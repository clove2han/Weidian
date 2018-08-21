# *- coding:utf8 *-
import sys
import os
from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash
from WeiDian.common.timeformat import format_for_db


sys.path.append(os.path.dirname(os.getcwd()))
from SBase import SBase, close_session
from WeiDian.models.model import SuperUser


class SSuperUser(SBase):
    
    @close_session
    def get_all_super(self):
        """获取所有的超级用户"""
        return self.session.query(SuperUser).filter_by(SUisdelete=False).all()

    @close_session
    def get_one_super_by_suid(self, suid):
        """通过suid获取超级用户"""
        super = self.session.query(SuperUser).filter_by(SUid=suid).first()
        if super:
            return super

    @close_session
    def verify_super(self, suname, supassword):
        """通过用户名和密码验证"""
        super = self.session.query(SuperUser).filter_by(SUname=suname).first()
        if super:
            if check_password_hash(super.SUpassword, supassword):
                return super