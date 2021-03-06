# *- coding:utf8 *-
import sys
import os
from datetime import datetime

from WeiDian.common.divide import Partner
from WeiDian.common.timeformat import format_for_db
from SBase import SBase, close_session
from WeiDian.models.model import HotMessage
sys.path.append(os.path.dirname(os.getcwd()))


class SHotMessage(SBase):

    @close_session
    def get_hotmsg_list_by_filter(self, htfilter):
        """正在进行中的热文"""
        filter_hotmsg = {HotMessage.HMisdelete == False}
        if isinstance(htfilter, list):
            filter_hotmsg.add(HotMessage.HMdisplaytype.in_(htfilter))
        else:
            filter_hotmsg.add(HotMessage.HMdisplaytype == htfilter)
        return self.session.query(HotMessage).filter(*filter_hotmsg).order_by(HotMessage.HMdisplaytype, HotMessage.HMsort.asc()).all()

        # hots = self.session.query(HotMessage).order_by(HotMessage.HMsort).all()
        # now_time = datetime.strftime(datetime.now(), format_for_db)
        # hots = filter(lambda ht: ht.HMstarttime < now_time < ht.HMendtime, hots)
        # # return hots
        # settings = Partner()
        # skiptype = settings.get_item('skip', 'skip_type')
        # return self.session.query(HotMessage).filter_by(HMisdelete=False, HMSkipType=skiptype).order_by(HotMessage.HMsort.asc()).all()

    # @close_session
    # def get_all_hot(self):
    #     hots = self.session.query(HotMessage).order_by(HotMessage.HMsort).all()
    #     return hots

    @close_session
    def add_one_hot(self, hot):
        self.session.add(hot)

    # @close_session
    # def update_one_hot(self, hmid, **kwargs):
    #     hotmessage = self.session.query(HotMessage).filter_by(HMid=hmid).first()
    #     if hotmessage:
    #         if 'hmtext' in kwargs.keys():
    #             hotmessage.HMtext = kwargs['hmtext']
    #         if 'prid' in kwargs.keys():
    #             hotmessage.PRid = kwargs['prid']
    #         if 'hmstarttime' in kwargs.keys():
    #             hotmessage.HMstarttime = kwargs['hmstarttime']
    #         if 'hmendtime' in kwargs.keys():
    #             hotmessage.HMendtime = kwargs['hmendtime']
    #         if 'hmsort' in kwargs.keys():
    #             hotmessage.HMsort = kwargs['hmsort']
    #         self.session.add(hotmessage)
    #         return True

    @close_session
    def update_hot_by_hmid(self, hmid, hotmessage):
        self.session.query(HotMessage).filter_by(HMid=hmid).update(hotmessage)
        return True

    @close_session
    def del_one_hot(self, hmid):
        return self.session.query(HotMessage).filter_by(HMid = hmid).delete()


    @close_session
    def get_hotmessage_by_filter(self, hot_filter):
        # settings = Partner()
        # skiptype = settings.get_item('skip', 'skip_type')
        # hot_filter.add(HotMessage.HMisdelete == False)
        # hot_filter.add(HotMessage.HMSkipType == skiptype)
        return self.session.query(HotMessage).filter(*hot_filter).first()

