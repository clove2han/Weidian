# *- coding:utf8 *-
import sys
import os
from datetime import datetime

from WeiDian.common.timeformat import format_for_db
from WeiDian.models.model import ShoppingCart

sys.path.append(os.path.dirname(os.getcwd()))
from SBase import SBase, close_session


class SShoppingCart(SBase):
    @close_session
    def get_shoppingcart_by_usid(self, usid):
        """根据用户搜索购物车"""
        return self.session.query(ShoppingCart).filter_by(USid=usid).all()

    @close_session
    def get_shoppingcart_by_usidandpid(self, usid, prid):
        """根据用户和商品搜索购物车"""
        return self.session.query(ShoppingCart).filter_by(USid=usid, PRid=prid).first()