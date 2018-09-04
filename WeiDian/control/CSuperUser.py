# *- coding:utf8 *-
import sys
import os
from flask import request
from WeiDian.common.token_required import usid_to_token
from WeiDian.common.import_status import import_status
from WeiDian.service.SSuperUser import SSuperUser
from WeiDian.config.response import PARAMS_MISS, SYSTEM_ERROR
sys.path.append(os.path.dirname(os.getcwd()))


class CSuperUser():
    def __init__(self):
        self.ssuperuser = SSuperUser()

    def login(self):
        """超级用户登录"""
        json_data = request.json
        suname = json_data.get('suname')
        supassword = json_data.get('supassword')
        if not suname or not supassword:
            return PARAMS_MISS
        suuser = self.ssuperuser.verify_super(suname, supassword)
        if not suuser:
            return SYSTEM_ERROR('用户名或密码错误')
        if suuser.SUlevel == 0:
            level = 'customerservice'
        if suuser.SUlevel == 1:
            level = 'ordinaryadmin'
        if suuser.SUlevel == 2:
            level = 'superadmin'
        token = usid_to_token(suuser.SUid, 'SuperUser')
        token_data = {
            'token': token,
            'level': level
        }
        data = import_status('generic_token_success', 'OK')
        data['data'] = token_data
        return data