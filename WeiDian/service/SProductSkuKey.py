# *- coding:utf8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))
from SBase import SBase, close_session
from WeiDian.models.model import ProductSkuKey


class SProductSkuKey(SBase):

    @close_session
    def get_psk_by_pid(self, prid):
        """通过prid获取所有的skukey"""
        return self.session.query(ProductSkuKey).filter_by(PRid=prid).all()

    @close_session
    def get_psk_by_pskid(self, pskid):
        """通过pskid获取"""
        return self.session.query(ProductSkuKey).filter_by(PSKid=pskid).first()
