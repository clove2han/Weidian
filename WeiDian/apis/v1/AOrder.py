# *- coding:utf8 *-
import sys
import os
from flask import jsonify
from flask_restful import Resource
from WeiDian.control.COrder import COrder
sys.path.append(os.path.dirname(os.getcwd()))


class AOrder(Resource):
    def __init__(self):
        self.corder = COrder()

    def post(self, order):
        print order
        apis = {
            'create': 'self.corder.add_one()',
            'send_order': 'self.corder.send_order()',
            'confim_order': 'self.corder.confim_order()',

         }
        res = eval(apis[order])
        return jsonify(res)

    def get(self, order):
        print order
        apis = {
            'get_more': 'self.corder.get_order_list()',
            'get_count': 'self.corder.get_order_count()',
            'get_list': 'self.corder.get_order_list_by_status()',
            'get_kd_list': 'self.corder.get_kd_list()',
            'admin_get_order_count': 'self.corder.admin_get_order_count()',
            'admin_get_order_list': 'self.corder.admin_get_order_list()',
            'get_order_info': 'self.corder.get_order_info()',  # 单个订单详情
        }
        res = eval(apis[order])
        return jsonify(res)
