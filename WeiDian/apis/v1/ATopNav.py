# *- coding:utf8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource

from WeiDian.control import CTopNav


class ATopNav(Resource):
    def __init__(self):
        self.ctopnav = CTopNav()

    def get(self, topnav):
        print topnav
        apis = {
            'get_all': 'self.ctopnav.get_all()',
        }
        res = eval(apis[topnav])
        return res

    def post(self, topnav):
        """添加首页上部导航"""
        print topnav
        apis = {
            'add_one': 'self.ctopnav.add_one()'
        }
        res = eval(apis[topnav])
        return res