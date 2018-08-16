# *- coding:utf8 *-
import sys
import os
from collections import namedtuple
from datetime import datetime

sys.path.append(os.path.dirname(os.getcwd()))
from SBase import SBase, close_session
from WeiDian.models.model import Activity
from WeiDian.common.filter_lasting import filter_lasting


# ActivityNameTuple = namedtuple('ActivityNameTuple', ['ACid',
#                                                'PRid',
#                                                'ACtype',
#                                                'ACtext',
#                                                'USid',
#                                                'AClikenum',
#                                                'AClikeFakeNum',
#                                                'ACbrowsenum',
#                                                'ACforwardnum',
#                                                'ACProductsSoldFakeNum',
#                                                'ACcreatetime',
#                                                'ACstarttime',
#                                                'ACendtime',
#                                                'ACistop', 'user', 'media', 'stags', 'foward_num'])


class SActivity(SBase):

    @close_session
    def get_activity_all(self):
        """所有活动
        返回活动对象列表"""
        activity_list = self.session.query(Activity).filter_by(ACisdelete=False).all()
        # activity_list = self.session.query(Activity.ACid, Activity.PRid, Activity.ACtype, Activity.TopnavId,
        #                                    Activity.ACtext,
        #                                    Activity.AClikenum, Activity.AClikeFakeNum, Activity.ACbrowsenum,
        #                                    Activity.ACforwardnum, Activity.ACProductsSoldFakeNum, Activity.ACcreatetime,
        #                                    Activity.ACstarttime, Activity.ACendtime, Activity.ACistop).filter_by(
        #     ACisdelete=False).all()
        return activity_list

    @close_session
    def get_activity_by_topnavid(self, navid):
        """根据导航的id获取活动"""
        acvitity_list = self.session.query(Activity).filter_by(ACisdelete=False, TopnavId=navid).order_by(Activity.ACcreatetime.desc()).all()
        # acvitity_list = self.session.query(Activity.ACid,
        #                                    Activity.PRid,
        #                                    Activity.ACtype,
        #                                    Activity.ACtext,
        #                                    Activity.USid,
        #                                    Activity.AClikenum,
        #                                    Activity.AClikeFakeNum,
        #                                    Activity.ACbrowsenum,
        #                                    Activity.ACforwardnum,
        #                                    Activity.ACProductsSoldFakeNum,
        #                                    Activity.ACcreatetime,
        #                                    Activity.ACstarttime,
        #                                    Activity.ACendtime,
        #                                    Activity.ACistop).filter_by(
        #     ACisdelete=False, TopnavId=navid).order_by(Activity.ACcreatetime.desc()).all()
        return acvitity_list

    @close_session
    def get_activity_by_usid(self, usid):
        acvitity_list = self.session.query(Activity).filter_by(ACisdelete=False, USid=usid).order_by(Activity.ACcreatetime.desc()).all()
        return acvitity_list

    @close_session
    def get_lasting_activity_by_topnavid(self, navid):
        """该导航下的所有正在进行的活动"""
        now_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
        all_activity = self.session.query(Activity).filter_by(ACisdelete=False, TopnavId=navid)
        # all_activity = self.session.query(Activity.ACid,
        #                                   Activity.PRid,
        #                                   Activity.ACtype,
        #                                   Activity.ACtext,
        #                                   Activity.USid,
        #                                   Activity.AClikenum,
        #                                   Activity.AClikeFakeNum,
        #                                   Activity.ACbrowsenum,
        #                                   Activity.ACforwardnum,
        #                                   Activity.ACProductsSoldFakeNum,
        #                                   Activity.ACcreatetime,
        #                                   Activity.ACstarttime,
        #                                   Activity.ACendtime,
        #                                   Activity.ACistop).filter_by(
        #     ACisdelete=False, TopnavId=navid)

        all_lasting_activity = all_activity.filter(now_time < Activity.ACendtime, now_time > Activity.ACstarttime).all()
        print all_lasting_activity
        return all_lasting_activity

    @close_session
    def add_activity(self, activity):
        self.session.add(activity)

    @close_session
    def delete_activity(self, acid):
        """
        根据活动id删除
        """
        cur_activity = self.session.query(Activity).filter_by(ACid=acid).first()
        cur_activity.ACisdelte = True
        self.session.add(cur_activity)

    @close_session
    def get_activity_by_acid(self, acid):
        """根据id获取活动"""
        return self.session.query(Activity).filter_by(ACid=acid, ACisdelete=False).first()
        # return self.session.query(
        #     Activity.ACid,
        #     Activity.GOid,
        #     Activity.ACtype,
        #     Activity.ACtext,
        #     Activity.AClikenum,
        #     Activity.AClikeFakeNum,
        #     Activity.ACbrowsenum,
        #     Activity.ACforwardnum,
        #     Activity.ACProductsSoldFakeNum,
        #     Activity.ACcreatetime,
        #     Activity.ACstarttime,
        #     Activity.ACendtime,
        #     Activity.ACistop).filter_by(ACid=acid, ACisdelete=False).first()

    @close_session
    def update_activity(self, activity):
        pass

    @close_session
    def foward_activity(self, forward):
        """转发活动"""
        self.session.add(forward)


if __name__ == '__main__':
    test = SActivity()
    res = test.get_activity_by_acid(1)
    import ipdb

    ipdb.set_trace()
    print(res)