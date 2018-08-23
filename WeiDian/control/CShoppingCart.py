# *- coding:utf8 *-

import uuid

from flask import request

from WeiDian.common.token_required import verify_token_decorator, is_tourist
from WeiDian.common.TransformToList import add_model, dict_add_models
from WeiDian.common.import_status import import_status
from WeiDian.config.response import PARAMS_MISS, TOKEN_ERROR
from WeiDian.control.BaseControl import BaseShoppingCart


class CShoppingCart(BaseShoppingCart):
    def __init__(self):
        from WeiDian.service.SShoppingCart import SShoppingCart
        self.sshoppingcart = SShoppingCart()
        from WeiDian.service.SProduct import SProduct
        self.sproduct = SProduct()
        from WeiDian.service.SProductSkuKey import SProductSkuKey
        self.sproductskukey = SProductSkuKey()

    @verify_token_decorator
    def get_shopingcart_all(self):
        """获取当前用户的购物车"""
        if not hasattr(request, 'user'):
            return TOKEN_ERROR  # token失效或者未携带token
        carts_list = self.sshoppingcart.get_shoppingcart_by_usid(request.user.id)
        map(self.fill_product, carts_list)
        map(self.fill_sku, carts_list)
        data = import_status('get_cart_success', "OK")
        data['data'] = carts_list
        return data


    @verify_token_decorator
    def update_shoppingcart(self):
        """购物车添加或者修改"""
        if is_tourist():
            return TOKEN_ERROR  # token无效或者未登录的用户
        data = request.json  
        # pskid 和 prid 至少需要一个, 如果用户选择的商品有psk则须使用pskid
        pskid = data.get('pskid')
        prid = data.get('prid')
        scnums = int(data.get('scnums'))
        usid = request.user.id
        if not pskid and not prid:
            return PARAMS_MISS
        cart = self.sshoppingcart.get_shoppingcart_by_usidandpid(usid, prid)
        if cart:  # 如果是存在的购物车记录
            scid = cart.SCid
            self.sshoppingcart.update_shoppingcart(cart, scnums)
        else:   # 如果没有则新建一个
            scid = str(uuid.uuid4())
            cartdict = {
                'scid': scid,
                'usid': usid,
                'pskid': pskid,
                'prid': prid,
                'scnums': scnums
            }
            dict_add_models('ShoppingCart', cartdict)
        data = import_status('update_cart_success', 'OK')
        data['data'] = {
            'scid': scid
        }
        return data
