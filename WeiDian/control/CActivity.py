# *- coding:utf8 *-
import sys
import os
from datetime import datetime

from sqlalchemy.orm import Session

from WeiDian.common.import_status import import_status
from WeiDian.common.timeformat import format_for_db

sys.path.append(os.path.dirname(os.getcwd()))
from flask import request
import json
import uuid


class CActivity():
    def __init__(self):
        from WeiDian.service.SActivity import SActivity
        self.sactivity = SActivity()
        from WeiDian.service.SActivityComment import SActivityComment
        self.sacomment = SActivityComment()
        from WeiDian.service.SActivityLike import SActivityLike
        self.salike = SActivityLike()
        from WeiDian.service.SUser import SUser
        self.suser = SUser()
        from WeiDian.service.SActivityMedia import SActivityMedia
        self.smedia = SActivityMedia()
        from WeiDian.service.SActivityTag import SActivityTag
        self.stags = SActivityTag()
        from WeiDian.service.SActivityFoward import SActivityFoward
        self.foward = SActivityFoward()
        self.session = Session()

    def get_all(self):
        """获取条件下的所有活动
        http://127.0.0.1:5000/activity/get_all?navid=q&lasting=true
        """
        args = request.args.to_dict()
        navid = args.get('navid')  # 导航id
        usid = args.get('usid')  # 用户id
        lasting = args.get('lasting', 'false')  # 是否正在进行的活动

        if navid:
            activity_list = self.sactivity.get_activity_by_topnavid(navid)
        if usid:
            activity_list = self.sactivity.get_activity_by_usid(usid)
        if lasting == 'true':
            now_time = datetime.strftime(datetime.now(), format_for_db)
            activity_list = filter(lambda act: True if act.ACstarttime < now_time < act.ACendtime else False, activity_list)
        print activity_list
        activity_list = map(dict, activity_list)
        activity_list = map(self.fill_detail, activity_list)
        data = import_status("get_product_list_success", "OK")
        data["data"] = activity_list
        return data

    def get_one(self):
        """通过id获取活动及活动下的评论"""
        args = request.args.to_dict()
        acid = args.get('acid')  # 活动id
        if acid:
            activity = self.sactivity.get_activity_by_acid(acid)
        else:
            pass
        activity = dict(activity)
        activity = self.fill_detail(activity)
        activity = self.fill_comment(activity)
        data = import_status("get_product_list_success", "OK")
        data["data"] = activity
        return data


    def fill_detail(self, act):
        """填充一些关联活动的信息"""
        acid = act['ACid']
        act['user'] = self.suser.get_user_by_user_id(act['USid'])
        act['media'] = self.smedia.get_media_by_acid(acid)  # 图片或视频
        act['tags'] = self.stags.get_show_tags_by_acid(acid)  # 右上角tag
        act['foward'] = self.foward.get_fowardnum_by_acid(acid)  # 转发数
        act['likenum'] = self.salike.get_likenum_by_acid(acid)  # 喜欢数
        return act

    def fill_comment(self, act):
        acid = act['ACid']
        act['comment'] = self.sacomment.get_comment_by_activity_id(acid)
        return act





