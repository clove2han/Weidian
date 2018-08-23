# *- coding:utf8 *   -
import uuid

from flask import request

from WeiDian.common.TransformToList import list_add_models, dict_add_models


class BaseControl():

    def is_admin_or_superadmin(self):
        return (request.user.scope == 'SuperUser' and request.user.SUlevel > 0)


class BaseActivityControl():

    def get_one_activity(self):
        pass

    def fill_detail(self, act):
        """填充一些关联活动的信息"""
        acid = act.ACid
        act.suuser = self.ssuperuser.get_one_super_by_suid(act.SUid)  # 超级用户
        act.media = self.smedia.get_media_by_acid(acid)  # 图片或视频
        act.tags = self.stags.get_show_tags_by_acid(acid)  # 右上角tag
        act.foward = self.foward.get_fowardnum_by_acid(acid)  # 转发数
        act.likenum = self.salike.get_likenum_by_acid(acid)  # 喜欢数
        act.soldnum = self.sactivity.get_product_soldnum_by_acid(acid)  # 销量
        act.add('suuser', 'media', 'tags', 'foward', 'likenum', 'soldnum')
        return act

    def fill_suser(self, obj):
        """给对象添加一个用户字段"""
        obj.suuser = self.suser.get_user_by_user_id(obj.USid)  # 对象的用户
        obj.add('user')
        return obj

    def fill_comment(self, act):
        """给活动对象附加一个评论属性"""
        acid = act.ACid
        act.comment = self.sacomment.get_comment_by_activity_id(acid)
        act.add('comment')
        map(self.fill_comment_apply_for, act.comment)
        return act

    def fill_comment_apply_for(self, comment):
        """"如果既是评论又是回复则添加一个'所回复用户'属性"""
        acoid = comment.ACOid
        if not comment.ACOparentid:
            return comment  # 如果ACOid没有值, 说明这不是回复的内容
        comment.parent_apply_user = self.sacomment.get_apply_for_by_acoid(acoid)
        comment.add('parent_apply_user')
        return comment


class BaseProductControl():

    def fix_product_list(self, items):
        """调整传入json数据列表,"""
        self.prid_list = []
        for item in items:
            prid = str(uuid.uuid4())  # 生成商品id
            self.prid_list.append(prid)
            psvid = str(uuid.uuid4())  # 每一个商品对应一个psv
            image_items = item.pop('images')  # 取出image列表
            sku_items = item.pop('sku')  # 获取sku的key列表, 用于填充至ProductSkuKey
            sku_value = item.get('sku_value')  # 获取sku的value列表
            item['prid'] = prid
            item['suid'] = request.user.id
            image_items = self.fix_image_list(image_items, prid)
            sku_items = self.fix_sku_list(sku_items, prid, psvid)
            productskuvalue = self.fix_sku_value(sku_value, prid, psvid)
            list_add_models('ProductImage', image_items)
            list_add_models('ProductSkuKey', sku_items)
            if productskuvalue:
                dict_add_models('ProductSkuValue', productskuvalue)
        return items

    def fix_image_list(self, image_items, prid):
        """为每一个image_item添加prid和piid"""
        if not image_items:
            return
        for image_item in image_items:
            image_item['piid'] = str(uuid.uuid4())
            image_item['prid'] = prid
        return image_items

    def fix_sku_list(self, sku_items, prid, psvid):
        """
        sku_items: sku列表
        prid: 商品id
        psvid: 对应的value表id
        功能: 为每一个psk_item添加pskid, prid, psvid"""
        if not sku_items:
            return
        for sku_item in sku_items:
            sku_item['pskid'] = str(uuid.uuid4())
            sku_item['prid'] = prid
            sku_item['psvid'] = psvid
            sku_item['pskproperkey'] = str(sku_item['pskproperkey'])
            # psk_key值是一个列表, 元素是个字典, 类似{key: 大小, value: xl}
        return sku_items

    def fix_sku_value(self, sku_value, prid, psvid):
        if not sku_value:
            return
        productskuvalue = {}
        productskuvalue['psvid'] = psvid
        productskuvalue['prid'] = prid
        productskuvalue['psvpropervalue'] = str(sku_value)
        return productskuvalue

    def fill_images(self, product):
        prid = product.PRid
        images_list = self.sproductimage.get_images_by_prid(prid)
        product.images = images_list
        product.add('images')
        return product

    def fill_product_sku_key(self, product):
        prid = product.PRid
        sku_list = self.sproductskukey.get_psk_by_pid(prid)
        if not sku_list:
            return
        for sku in sku_list:
            sku.PSKproperkey = eval(sku.PSKproperkey)
        product.sku = sku_list
        product.add('sku')
        return product

    def fill_product_sku_value(self, product):
        prid = product.PRid
        sku_value = self.sproductskuvalue.get_skvalue_by_prid(prid)
        if not sku_value:
            return
        sku_value.PSVpropervalue = eval(sku_value.PSVpropervalue)
        product.sku_value = sku_value
        product.add('sku_value')
        return product

    def fill_activity(self, product):
        prid = product.PRid
        activity_list = self.activity.get_activiti_by_prid(prid)
        product.activity = activity_list
        product.add('activity')
        return product

    def trans_product_for_fans(self, product):
        """调整为粉丝版本"""
        # 粉丝页面显示本身价格和店主价, 以及相关商品推荐(规则?)
        prkeeperprice = product.PRprice * self.partner.new_partner
        product.prkeeperprice = prkeeperprice
        product.add('prkeeperprice')
        return product

    def trans_product_for_shopkeeper(self, product):
        """调整为店主版本"""
        # 店主页面需要显示赚多少, '买'和'卖'分别省多少和赚多少(10%)
        # 暂定为赚取金额为店主价-普通价格
        prkeeperprice = product.PRprice * self.partner.new_partner
        # 节省或赚取的价格
        product.prsavemonty = product.PRprice - prkeeperprice
        product.add('prsavemonty')
        return product
    
    def fill_product_nums(self, product):
        prid = product.PRid
        soldnum = product.PRsalefakenum or product.PRsalesvolume  # 显示销量
        viewnum = product.PRfakeviewnum or product.PRviewnum  # 浏览数
        likenum = product.PRfakelikenum or self.sproductlike.get_product_like_num_by_prid(prid)  # 收藏(喜欢)数目
        product.prsoldnum = soldnum
        product.prviewnum = viewnum
        product.prlikenum = likenum
        product.add('prsoldnum', 'prlikenum', 'prviewnum') 
        return product
