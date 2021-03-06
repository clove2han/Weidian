# -*- coding:utf8 -*-
import json
import re
import sys
import os
import uuid

import requests

from WeiDian import logger
from WeiDian.common.divide import Partner
from WeiDian.common.get_model_return_list import get_model_return_dict
from WeiDian.common.import_status import import_status
from WeiDian.common.params_require import parameter_required
from WeiDian.common.token_required import verify_token_decorator, is_tourist, is_partner, is_admin
from WeiDian.config.enums import BANK_MAP, finished_pay_status, userlevel
from WeiDian.config.response import AUTHORITY_ERROR, SYSTEM_ERROR, TOKEN_ERROR, PARAMS_ERROR, TIME_ERROR, PARAMS_MISS, \
    NOT_FOUND
from WeiDian.control.BaseControl import BaseMyCenterControl
from flask import request

from WeiDian.service.SOrder import SOrder
from WeiDian.service.SPartnerSellOrInviteMatch import SPartnerSellOrInviteMatch
from WeiDian.service.SRaward import SRaward
from WeiDian.service.STopNav import STopNav

sys.path.append(os.path.dirname(os.getcwd()))


class CMyCenter(BaseMyCenterControl):
    def __init__(self):
        from WeiDian.service.SProduct import SProduct
        self.sproduct = SProduct()
        from WeiDian.service.SUser import SUser
        self.suser = SUser()
        from WeiDian.service.SMyCenter import SMyCenter
        self.smycenter = SMyCenter()
        from WeiDian.service.SLevelRules import SLevelRules
        self.slevelrules = SLevelRules()
        from WeiDian.service.SUserAddress import SUserAddress
        self.suesraddress = SUserAddress()
        from WeiDian.service.SBankCard import SBankCard
        self.sbankcard = SBankCard()
        self.sorder = SOrder()
        self.sraward = SRaward()
        self.spartnermatch = SPartnerSellOrInviteMatch()
        self.stopnav = STopNav()

    @verify_token_decorator
    def get_info_top(self):
        """个人中心需要的数据"""
        try:
            if is_tourist():
                return AUTHORITY_ERROR(u"未登录")
            data = dict()
            my_info = request.user
            level = my_info.level
            uslevel = userlevel.get(str(level), '普通用户')
            level = 'partner' if level > 0 else 'ordinary'

            my_info.fill(level, 'level')
            my_info.fill(uslevel, 'uslevel')
            data.setdefault('user', my_info)
            usid = my_info.id
            print (my_info.USname).encode('utf8')
            print (my_info.USid).encode('utf8')
            logger.debug("get my info by usid")
            show = 0
            # 正在进行中的指定等级的合伙人活动
            partner_match = self.spartnermatch.get_lasting_partner_match(level=my_info.USlevel)
            # 如果是合伙人, 且活动进行中
            if is_partner() and partner_match:
                show = 1
                data.setdefault('match_type', partner_match.PSIMtype)
                # 成功超过vip数量
                psimid = partner_match.PSIMid
                my_achev = self.spartnermatch.get_partner_match_mount_by_usidpsmid(usid, psimid)
                my_achev_value = my_achev.sellorinvitemount if my_achev else 0  # 我的销售总额(人数)

                gt_my_sell_count = self.spartnermatch.get_partner_match_mount_gt_value(psimid, my_achev_value)   # 营业额(人数)比我多的
                partner_num = self.suser.get_partner_count_in_current_level(request.user.USlevel)  # 该等级vip总数
                lt_my_sell_count = partner_num - gt_my_sell_count  # 比我销售(人数)少的
                partner_num = partner_num or 1
                percents = int(float(lt_my_sell_count) / partner_num * 100)   # 超过的同等级的百分比
                my_info.fill(percents, 'overpercents')  # 超过%的vip
                data.setdefault('myranking', percents)
                # 未完成还需多少升级
                try:
                    partner_match.PSIMrule = match_rule = json.loads(partner_match.PSIMrule)
                    achev_level_value = {k: int(v) - my_achev_value for k, v in match_rule.items() if int(v) > my_achev_value}
                    #
                    if achev_level_value:  # 是否有下一级
                        next_level = sorted(achev_level_value.keys())[0]
                        # 当前等级(未用到)
                        current_level = int(next_level) - 1
                        to_next = achev_level_value[next_level]
                        my_info.fill(to_next, 'next')
                        data.setdefault('next', to_next)
                    else:
                        my_info.fill(0, 'next')
                        current_level = sorted(achev_level_value.keys())[-1]

                except ValueError as e:
                    print('保级错误')
                    my_info.fill('0', 'next')
                #     pass
                # 保级差别
            response = import_status("get_my_info_success", "OK")
            data.setdefault('show', show)
            response["data"] = data
            return response
        except Exception as e:
            logger.exception("get myinfo error")
            raise SYSTEM_ERROR()

    @verify_token_decorator
    def set_schedual_show(self):
        """设置个人主页升级进度显示(vip数据统计), 素材圈显示, 待评价"""
        if not is_admin():
            raise TOKEN_ERROR(u'请使用管理员登录')
        # data = parameter_required(u'vip_match', u'material', u'wait_apply')
        data = request.json
        paras_list = ['vip_match', 'material', 'wait_apply']
        if not data or not filter(lambda x: x in paras_list, data):
            raise PARAMS_MISS()
        if 'vip_match' in data:  # vip进度, 写在model里
            vip_match_show = False if str(data.get('vip_match')) == '1' else True
            updated = self.spartnermatch.update_partner_match(1, {  # 更改: 这里的level没有用
                'PSIMisclose': vip_match_show
            })
        if 'material' in data:  # 素材圈是否显示, 写在model里
            material_show = False if str(data.get('material')) == '1' else True
            updated = self.stopnav.update_topnav_by_tnidorname(data={
                'Tisdelete': material_show
            }, name='素材圈')

        if 'wait_apply' in data:  # 写在配置文件里
            wait_apply_show = data.get('wait_apply')
            wait_apply_show = '0' if str(wait_apply_show) == '0' else '1'
            Partner().set_item('show', 'wait_apply', wait_apply_show)
        msg = 'update_success'
        data = import_status(msg, "OK")
        return data

    def get_schedual_show(self):
        """获取控制中心显示隐藏详情"""
        match = self.spartnermatch.get_lasting_partner_match(level=1)
        vip_match = 1 if match else 0
        mater = self.stopnav.get_topnav_by_name('素材圈')
        material = 0 if mater.Tisdelete else 1
        wait_apply = Partner().get_item('show', 'wait_apply')
        data = import_status('get_success', 'OK')
        data['data'] = {
            'vip_match': vip_match,
            'material': material,
            'wait_apply': wait_apply,
        }
        return data

    @verify_token_decorator
    def get_today_total(self):
        """今日"""
        if not is_partner():
            raise TOKEN_ERROR(u'请使用vip登录')
        usid = request.user.id
        # 今日营业额
        today_orders = self.sorder.get_today_order_by_usid_status(usid, finished_pay_status)
        sold_mount_list = [x.OImount for x in today_orders] or [0]
        sold_mount = sum(sold_mount_list)
        # 今日赚
        today_earn = sold_mount * Partner().one_level_divide
        today_earn = round(today_earn, 2)
        # 额外赚
        # todo
        other_earn = 0
        # 新衣币
        new_cloth_bit = self.sraward.get_reward_by_usid(usid)
        bit_num_list = [x.RAnumber for x in new_cloth_bit] or [0]
        bit_num_mount = sum(bit_num_list)
        response = import_status('get_today_earn_success', 'OK')
        data = {
            'sold_mount': sold_mount,
            'today_earn': today_earn,
            'other_earn': other_earn,
            'bit_num_mount': bit_num_mount
        }
        response['data'] = data
        return response


    @verify_token_decorator
    def get_levelrules(self):
        if is_tourist():
            return AUTHORITY_ERROR(u"未登录")
        try:
            lr_list = self.slevelrules.get_rule_list()
            logger.debug("get level rules")
            map(lambda x: setattr(x, 'LRtext', re.sub('\s', '', x.LRtext)), lr_list)
            user = self.suser.get_user_by_user_id(request.user.id)
            if user.USlevel == 0:
                user.level = 'ordinary'
            if user.USlevel > 0:
                user.level = 'partner'
            user.add('level').hide('USid', 'USname', 'USheader')
            data = import_status("get_levelrules_success", "OK")
            data['data'] = lr_list
            data['userlevel'] = user.level
            return data
        except:
            logger.exception("get level rules error")
            return SYSTEM_ERROR

    @verify_token_decorator
    def get_accountinfo(self):
        if is_tourist():
            return AUTHORITY_ERROR(u"未登录")
        usid = request.user.id
        user = self.suser.get_user_by_user_id(usid)
        logger.debug("get info success, this user is %s", user.USname)
        default_address = self.suesraddress.get_default_address_by_usid(usid)
        if not default_address:
            first_address = self.suesraddress.get_first_no_default_address(usid)
        address = default_address or first_address
        if address:
            logger.info("get user address success")
            location = self.suesraddress.get_addressinfo_by_areaid(address.areaid)
            logger.info("get address detail success")
            for area, city, provice in location:
                locationname = getattr(provice, "name", '') + getattr(city, "name", '') + getattr(area, "name", '')
        else:
            locationname = ''
        # print ''.join([x[1] for x in area])
        bankcard = self.sbankcard.get_bankcard_by_usid(usid)
        response = import_status("get_accountinfo_success", "OK")
        response['data'] = {
            "user": user.hide('USid'),
            # "address": '%s%s' %(locationname, address.UAtext),
            "address": '%s%s' % (locationname, getattr(address, "UAtext", '')),
            "bankcard": getattr(bankcard, "BCnumber", '')
        }
        return response

    """用户地址信息"""
    @verify_token_decorator
    def get_useraddress(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR(u"未登录, 或token错误")
        try:
            adderss_list = self.suesraddress.get_address_list_by_usid(request.user.id)
            logger.debug("get address list")
            self.fill_areainfo_by_areaid(adderss_list)
            data = import_status("get_useraddress_success", "OK")
            data['data'] = adderss_list
            return data
        except:
            logger.exception("get useraddress by usid error ")
            return SYSTEM_ERROR

    def fill_areainfo_by_areaid(self, address_list):
        for address in address_list:
            adr = self.suesraddress.get_address_by_uaid(address.UAid)
            addressinfoes = self.suesraddress.get_addressinfo_by_areaid(adr.areaid)
            for addressinfo in addressinfoes:
                address.addressinfo = addressinfo
                address.add("addressinfo")
        return address_list

    @verify_token_decorator
    def get_one_or_default_address(self):
        if is_tourist():
            raise TOKEN_ERROR(u'未登录')
        uaid = request.args.to_dict().get('uaid')
        usid = request.user.id
        logger.debug("get uaid is %s", uaid)
        if uaid is not None:
            uafilter = {'UAid': uaid}
        else:
            uafilter = {'USid': usid,
                        'UAdefault': True,
                        'UAisdelete': False
                        }
        default_address = self.suesraddress.get_one_or_default_address(uafilter)
        if not default_address:
            any_address =self.suesraddress.get_first_no_default_address(usid)
            if not any_address:
                raise NOT_FOUND(u'该用户未设置地址信息')
        address = default_address or any_address
        if address:
            logger.info("get address success, now to fill detail")
        addressinfoes = self.suesraddress.get_addressinfo_by_areaid(address.areaid)
        for addressinfo in addressinfoes:
            address.addressinfo = addressinfo
            address.add("addressinfo")
        response = import_status("messages_get_item_ok", "OK")
        response['data'] = address
        return response

    @verify_token_decorator
    def add_useraddress(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR(u"未登录, 或token错误")
        parameter_required("areaid", "UAname", "UAphone", "UAtext")
        data = request.json
        logger.info("this is useraddress data %s", data)
        try:
            uaid = str(uuid.uuid1())
            logger.debug("get default address by usid")
            exist_default = self.suesraddress.get_default_address_by_usid(request.user.id)
            uadefault = True if not exist_default else data.get("UAdefault")
            if str(uadefault) not in ['True', 'False']:
                raise PARAMS_ERROR(u'uadefault参数不合法')
            if uadefault is True and exist_default:
                self.suesraddress.change_default_address_status(exist_default.UAid, {'UAdefault': False})
            self.suesraddress.add_model("UserAddress", **{
                "UAid": uaid,
                "USid": request.user.id,
                "UAname": data.get("UAname"),
                "UAphone": data.get("UAphone"),
                "UAtext": data.get("UAtext"),
                "areaid": data.get("areaid"),
                "UAdefault": uadefault
            })
            response = import_status("add_address_success", "OK")
            response['data'] = {
                "UAid": uaid
            }
            return response
        except:
            logger.exception("add user address error")
            return SYSTEM_ERROR

    @verify_token_decorator
    def update_address(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR(u"未登录, 或token错误")
        args = request.args.to_dict()
        logger.debug("this is address args %s", args)
        data = request.json
        logger.debug("this is address data %s", data)
        uaid = args.get('uaid')
        uadefault = data.get("UAdefault")
        try:
            exist_default = self.suesraddress.get_default_address_by_usid(request.user.id)
            parameter_required("uaid", "areaid", "UAname", "UAphone", "UAtext", "UAdefault")
            if uadefault == True and exist_default:
                self.suesraddress.change_default_address_status(exist_default.UAid, {'UAdefault': False})
            update_address = self.suesraddress.update_address(uaid, {"areaid": data.get("areaid"),
                                                                    "UAname": data.get("UAname"),
                                                                    "UAphone": data.get("UAphone"),
                                                                    "UAtext": data.get("UAtext"),
                                                                    "UAdefault": uadefault
                                                                    })
            logger.info("update address succress ")
            if not update_address:
                raise SYSTEM_ERROR(u'数据更新错误')
            response = import_status("update_useraddress_success", "OK")
            response['data'] = {"uaid": args["uaid"]}
            return response
        except:
            logger.exception("update address error")
            return SYSTEM_ERROR

    @verify_token_decorator
    def del_address(self):
        if is_tourist():
            return TOKEN_ERROR(u"未登录, 或token错误")
        data = request.json
        logger.info("this is del address data %s", data)
        parameter_required("UAid")
        try:
            logger.debug("del address")
            del_address = self.suesraddress.delete_address(data.get("UAid"))
            if not del_address:
                return SYSTEM_ERROR
            exist_default = self.suesraddress.get_default_address_by_usid(request.user.id)
            if not exist_default:
                no_default_address = self.suesraddress.get_first_no_default_address(request.user.id)
                if no_default_address:
                    self.suesraddress.change_default_address_status(no_default_address.UAid, {'UAdefault': True})
            response = import_status("delete_useraddress_success", "OK")
            response['data'] = {"uaid": data.get("UAid")}
            return response
        except:
            logger.exception("del address error")
            return SYSTEM_ERROR

    """省市区地址"""
    def get_province(self):
        try:
            province_list = self.suesraddress.get_province()
            logger.debug("get province")
            # map(lambda x: x.hide('_id'), province_list)
            res = import_status("get_province_list_success", "OK")
            res["data"] = province_list
            return res
        except:
            logger.exception("get province error")
            return SYSTEM_ERROR

    def get_city_by_provincenum(self):
        args = request.args.to_dict()
        logger.info("get city list args is %s", args)
        parameter_required("provinceid")
        province_id = args["provinceid"]
        try:
            logger.debug("get citylist by province_id")
            city_list = self.suesraddress.get_citylist_by_provinceid(province_id)
            # map(lambda x: x.hide('_id'), city_list)
            res = import_status("get_city_list_success", "OK")
            res["data"] = city_list
            return res
        except:
            logger.exception("get city list error")
            return SYSTEM_ERROR

    def get_area_by_citynum(self):
        args = request.args.to_dict()
        logger.info("get area args is %s", args)
        parameter_required('cityid')
        city_id = args['cityid']
        try:
            logger.debug("get arealist by cityid")
            area_list = self.suesraddress.get_arealist_by_cityid(city_id)
            # map(lambda x: x.hide('_id'), area_list)
            res = import_status("get_area_list_success", "OK")
            res["data"] = area_list
            return res
        except:
            logger.exception("get area list error")
            return SYSTEM_ERROR

    """银行卡部分"""
    @verify_token_decorator
    def add_bankcard(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR(u"未登录, 或token错误")
        data = request.json
        logger.info("this add bankcard info %s", data)
        parameter_required('BCusername', 'BCnumber', 'BCbankname', 'BCaddress')
        banknumber = str(data.get('BCnumber')).strip()
        self._verify_cardnum(banknumber, error='raise')
        usid = request.user.id
        try:
            bankcard = self.sbankcard.update_bankcard_by_usid(usid, {
                'BCisdelete': True
            })
            logger.debug("bankcard count is %s", bankcard)
            bcid = str(uuid.uuid1())
            self.sbankcard.add_model("BankCard", **{
                "BCid": bcid,
                "USid": usid,
                "BCusername": data.get("BCusername"),
                "BCnumber": banknumber,
                "BCbankname": data.get("BCbankname"),
                "BCaddress": data.get("BCaddress")
            })
            response = import_status("add_bank_card_success", "OK")
            response['data'] = {"BCid": bcid}
            return response
        except:
            logger.exception("add bankcard error")
            return SYSTEM_ERROR

    @verify_token_decorator
    def get_bankcard(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR(u"未登录, 或token错误")
        args = request.args.to_dict()
        logger.info("get bankcard this is args %s", args)
        try:
            logger.debug("get bankcard")
            my_bankcard = self.sbankcard.get_bankcard_by_usid(request.user.id)

            if not my_bankcard or not my_bankcard.BCnumber or not my_bankcard.BCusername:
                my_bankcard = None

            response = import_status("get_bankcard_success", "OK")
            response['data'] = my_bankcard
            return response
        except:
            logger.exception("get bankcard error")
            return SYSTEM_ERROR

    @verify_token_decorator
    def del_bankcard(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR(u"未登录, 或token错误")
        data = request.json
        logger.info("this is del bankcard data %s", data)
        parameter_required("BCid")
        try:
            logger.debug("del bankcard")
            del_bankcard = self.sbankcard.del_bankcard(data.get("BCid"), request.user.id)
            if not del_bankcard:
                return SYSTEM_ERROR
            response = import_status("delete_bankcard_success", "OK")
            response['data'] = {"bcid": data.get("BCid")}
            return response
        except:
            logger.exception("del address error")
            return SYSTEM_ERROR

    @verify_token_decorator
    def update_bankcard(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR(u"未登录, 或token错误")
        args = request.args.to_dict()
        logger.info("this is update bankcard args %s", args)
        data = request.json
        logger.info("this is update bankcard data %s", data)
        try:
            parameter_required("bcid", "BCusername", "BCnumber", "BCbankname", "BCaddress")
            update_bankcard = self.sbankcard.update_bankcard(args["bcid"], data)
            logger.debug("update bankcard accress")
            if not update_bankcard:
                return SYSTEM_ERROR
            response = import_status("update_bankcard_success", "OK")
            response["data"] = {"bcid": args["bcid"]}
            return response
        except:
            logger.exception("update bankcard error")
            return SYSTEM_ERROR

    @verify_token_decorator
    def get_bankname_list(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR(u"未登录, 或token错误")
        data = import_status("get_useraddress_success", "OK")
        data['data'] = BANK_MAP
        return data

    """发送/校验验证码"""
    @verify_token_decorator
    def get_inforcode(self):
        # return TIME_ERROR
        if not hasattr(request, 'user'):
            return TOKEN_ERROR(u"未登录, 或token错误")
        user = self.suser.get_user_by_user_id(request.user.id)
        if not user:
            return SYSTEM_ERROR
        Utel = user.USphone
        # 拼接验证码字符串（6位）
        code = ""
        while len(code) < 6:
            import random
            item = random.randint(1, 9)
            code = code + str(item)

        # 获取当前时间，与上一次获取的时间进行比较，小于60秒的获取直接报错
        import datetime
        from WeiDian.common.timeformat import format_for_db
        time_time = datetime.datetime.now()
        time_str = datetime.datetime.strftime(time_time, format_for_db)

        # 根据电话号码获取时间
        time_up = self.smycenter.get_uptime_by_utel(Utel)
        logger.debug("this is time up %s", time_up)

        if time_up:
            time_up_time = datetime.datetime.strptime(time_up.ICtime, format_for_db)
            delta = time_time - time_up_time
            if delta.seconds < 60:
                return import_status("ERROR_MESSAGE_GET_CODE_FAST", "WEIDIAN_ERROR", "ERROR_CODE_GET_CODE_FAST")

        new_inforcode = self.smycenter.add_inforcode(Utel, code, time_str)

        logger.debug("this is new inforcode %s ", new_inforcode)

        if not new_inforcode:
            return SYSTEM_ERROR
        from WeiDian.config.Inforcode import SignName, TemplateCode
        from WeiDian.common.Inforsend import send_sms
        params = '{\"code\":\"' + code + '\",\"product\":\"etech\"}'

        # params = u'{"name":"wqb","code":"12345678","address":"bz","phone":"13000000000"}'
        __business_id = uuid.uuid1()
        response_send_message = send_sms(__business_id, Utel, SignName, TemplateCode, params)

        response_send_message = json.loads(response_send_message)
        logger.debug("this is response %s", response_send_message)

        if response_send_message["Code"] == "OK":
            status = 200
        else:
            status = 405
        # 手机号中四位替换为星号
        # response_ok = {"usphone": Utel[:3] + '****' + Utel[-4: ]}
        response_ok = {"usphone": Utel}
        response_ok["status"] = status
        response_ok["messages"] = response_send_message["Message"]

        return response_ok

    @verify_token_decorator
    def verify_inforcode(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR(u"未登录, 或token错误")
        data = request.json
        user = self.suser.get_user_by_user_id(request.user.id)
        codeinfo = self.smycenter.get_inforcode_by_usphone(user.USphone)
        if not codeinfo:
            return SYSTEM_ERROR(u"用户验证信息错误")
        iccode = data.get("ICcode")
        verifystatus = True if iccode == codeinfo.ICcode else False
        verifymessage = u"验证码正确" if verifystatus is True else u"验证码错误"
        response = import_status("verify_inforcode_access", "OK")
        response["data"] = {"verifystatus": verifystatus,
                            "verifymessage": verifymessage
                            }
        return response

    def _verify_cardnum(self, num, error='ignore'):
        """获取所属行"""
        bank_url = 'https://ccdcapi.alipay.com/validateAndCacheCardInfo.json?cardNo={}&cardBinCheck=true'
        url = bank_url.format(num)
        response = requests.get(url).json()
        bank = response.get('bank')
        if not bank and error != 'ignore':
            raise SYSTEM_ERROR(u'卡号无效')
        return bank

    """设置获取微信分享参数"""
    @verify_token_decorator
    def set_share_params(self):
        if not is_admin():
            raise TOKEN_ERROR(u'请使用管理员登录')
        data = request.json
        title = data.get('title')
        # title = title.encode("utf8") if isinstance(title, unicode) else title

        content = data.get('content')
        img = data.get('img')


        parameter_required('title', 'content', 'img')
        Partner().set_item('share', 'title', title)
        Partner().set_item('share', 'content', content)
        Partner().set_item('share', 'img', img)
        response = import_status('set_success', 'OK')
        return response

    @verify_token_decorator
    def get_share_params(self):

        args = request.args.to_dict()
        prid = args.get('prid')
        logger.debug("get share params args is %s", args)
        if prid:
            from WeiDian.service.SActivity import SActivity
            actext_by_prid = get_model_return_dict(SActivity().get_one_act_by_prid(prid))['ACtext']
            title = actext_by_prid.split(u'。')[0]
            content = actext_by_prid.split(u'。')[-1]
            img = get_model_return_dict(self.sproduct.get_prmainpic_by_prid(prid))['PRmainpic']
        else:
            settings = Partner()
            title = settings.get_item('share', 'title')
            content = settings.get_item('share', 'content')
            img = settings.get_item('share', 'img')
        response = import_status("messages_get_item_ok", "OK")
        response['data'] = {'title': title,
                            'content': content,
                            'img': img
                            }
        return response








