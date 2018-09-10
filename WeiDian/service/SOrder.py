# *- coding:utf8 *-
import sys
import os

from WeiDian.models.model import OrderInfo, OrderProductInfo

sys.path.append(os.path.dirname(os.getcwd()))
from SBase import SBase, close_session


class SOrder(SBase):

    @close_session
    def get_order_by_usid(self, sell, usid, page_num, page_size):
        """获取用户的订单"""
        if sell:
            return self.session.query(OrderInfo).filter_by(Sellerid=usid, OIisdelete=False).order_by(
                OrderInfo.OIcreatetime).offset(page_size * (page_num - 1)).limit(page_size).all()
        else:
            return self.session.query(OrderInfo).filter_by(USid=usid, OIisdelete=False).order_by(
                OrderInfo.OIcreatetime).offset(page_size * (page_num - 1)).limit(page_size).all()

    @close_session
    def get_order_by_oiid(self, oiid):
        """根据订单id获取订单"""
        return self.session.query(OrderInfo).filter_by(OIid=oiid, OIisdelete=False).first()

    @close_session
    def get_user_order_by_status(self, usid, status, page_num, page_size):
        """根据支付状态获取自买订单"""
        return self.session.query(OrderInfo).filter_by(USid=usid, OIpaystatus=status).order_by(
            OrderInfo.OIcreatetime).offset(page_size * (page_num - 1)).limit(page_size).all()

    @close_session
    def get_sell_order_by_status(self, usid, status, page_num, page_size):
        """根据支付状态获取销售订单"""
        return self.session.query(OrderInfo).filter_by(Sellerid=usid, OIpaystatus=status).order_by(
            OrderInfo.OIcreatetime).offset(page_size * (page_num - 1)).limit(page_size).all()

    @close_session
    def get_user_ordercount_by_status(self, usid, status):
        """获取自买订单预览数"""
        return self.session.query(OrderInfo).filter_by(
            USid=usid, OIpaystatus=status).count()

    @close_session
    def get_sell_ordercount_by_status(self, usid, status):
        """获取销售订单预览数"""
        return self.session.query(OrderInfo).filter_by(
            Sellerid=usid, OIpaystatus=status).count()

    @close_session
    def get_order_by_oisn(self, oisn):
        """根据订单号获取订单"""
        return self.session.query(OrderInfo).filter_by(OIsn=oisn).first()

    @close_session
    def get_orderinfowithproduct_by_opiid(self, oiid):
        """联合查询测试"""
        return self.session.query(OrderInfo).join(
            OrderProductInfo,
            OrderInfo.OIid == OrderProductInfo.OIid).filter(
            OrderInfo.OIid == oiid).all()

    @close_session
    def get_orderproductinfo_by_oiid(self, oiid):
        return self.session.query(
            OrderProductInfo).filter_by(OIid=oiid).first()
