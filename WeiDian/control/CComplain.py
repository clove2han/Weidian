# *- coding:utf8 *-
import sys
import os
import uuid
import re

from WeiDian.common.timeformat import get_web_time_str
from flask import request
from WeiDian.config.response import TOKEN_ERROR, PARAMS_MISS, SYSTEM_ERROR
from WeiDian.common.import_status import import_status
from WeiDian.common.params_require import parameter_required
from WeiDian.common.token_required import verify_token_decorator, is_admin
sys.path.append(os.path.dirname(os.getcwd()))
from WeiDian import logger


class CComplain():
    def __init__(self):
        from WeiDian.service.SComplain import SComplain
        self.scomplain = SComplain()
        from WeiDian.service.SActivity import SActivity
        self.sactivity = SActivity()
        from WeiDian.service.SUser import SUser
        self.suser = SUser()

    @verify_token_decorator
    def get_complain_by_usid(self):
        """后台管理查看投诉记录"""
        if not hasattr(request, 'user'):
            raise TOKEN_ERROR()  # 未登录, 或token错误
        args = request.args.to_dict()
        logger.debug("get complain args is %s", args)
        page_size = args.get('page_size')
        page_size = 10 if not page_size else int(page_size)
        page_num = args.get('page_num')
        page_num = 1 if not page_num else int(page_num)
        try:
            complain_list = self.scomplain.admin_get_all_complain(page_size, page_num)
            complain_list_length = self.scomplain.admin_get_complain_count()
            from WeiDian.config.enums import complain_type
            data = import_status("get_complain_success", "OK")
            for complain in complain_list:
                colist = str(complain.COtype).split(",")
                logger.debug('get colist %s', colist)
                complaintype = "，".join([complain_type.get(i) for i in colist])
                logger.debug('convert complain type %s', complaintype)
                complain.COtype = complaintype
                user_info = self.suser.get_user_by_user_id(complain.USid)
                complain.fill(user_info.USname, 'usname')
                complain.COcreatetime = get_web_time_str(complain.COcreatetime)

            data['data'] = complain_list
            data['count'] = complain_list_length
            logger.debug("get complain by usid %s", complain_list)
            return data
        except:
            logger.exception("get complain by usid error")
            raise SYSTEM_ERROR(u'获取数据错误')

    @verify_token_decorator
    def add_complain(self):
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # 未登录, 或token错误
        parameter_required("OIid", "COtype")
        data = request.json
        try:
            complain = self.scomplain.get_complain_by_oiid(data.get("OIid"))
            logger.debug("get complain by oiid %s", complain)
            if complain:
                return import_status("complain_repeat_error", "WD_ERROR", "error_complain_exit")
            coid = str(uuid.uuid1())
            cotype_list = [str(i) for i in data.get("COtype", [])]

            self.scomplain.add_model("Complain", **{
                "COid": coid,
                "COcontent": data.get("COcontent"),
                "COtype": ",".join(cotype_list),
                "OIid": data.get("OIid"),
                "USid": request.user.id,
                "COtreatstatus": 1,
            })
            response = import_status("complain_success", "OK")
            response['data'] = {
                "COid": coid
            }
            return response
        except:
            logger.exception("add complain error")
            return SYSTEM_ERROR

    # @verify_token_decorator
    def update_status(self):
        # if not is_admin():
        #     raise TOKEN_ERROR
        parameter_required('coid', 'cotreatstatus')
        data = request.json
        logger.debug('get update complain status %s', data)
        complain = self.scomplain.get_complain_by_coid(data.get("coid"))
        if not complain:
            raise PARAMS_MISS('params coid is not right')
        if not re.match(r'^[0-2]$', str(data.get("cotreatstatus"))):
            raise PARAMS_MISS('params cotreatstatus is not right')
        cotreatstatus = int(data.get("cotreatstatus"))
        if cotreatstatus <= complain.COtreatstatus:
            raise PARAMS_MISS('params cotreatstatus is not right')
        update_result = self.scomplain.update_complain(data.get("coid"), {"COtreatstatus": cotreatstatus})
        if not update_result:
            raise SYSTEM_ERROR(u"服务器繁忙")
        return import_status('update_complain_success', "OK")

