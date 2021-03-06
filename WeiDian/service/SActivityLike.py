# *- coding:utf8 *-
import sys
import os
from SBase import SBase, close_session
from WeiDian.models.model import ActivityLike, Activity
sys.path.append(os.path.dirname(os.getcwd()))


class SActivityLike(SBase):

    @close_session
    def get_likenum_by_acid(self, acid):
        """获得活动的点赞或虚拟数量"""
        cur_activity = self.session.query(Activity).filter_by(ACid=acid).first()
        if cur_activity.AClikeFakeNum:
            return cur_activity.AClikeFakeNum
        return cur_activity.AClikenum

    @close_session
    def add_like(self, aclike):
        """添加喜欢数量"""
        acid = aclike.acid
        cur_activity = self.session.query(Activity).filter_by(ACid=acid).first()
        if cur_activity.AClikeFakeNum:
            cur_activity.AClikeFakeNum += 1
            self.session.add(cur_activity)
        self.session.add(aclike)

    @close_session
    def add_like_by_acid(self, acid):
        cur_activity = self.session.query(Activity).filter_by(ACid=acid).first()
        if cur_activity.AClikeFakeNum:
            cur_activity.AClikeFakeNum += 1
        else:
            cur_activity.AClikenum += 1
        self.session.add(cur_activity)
        # self.session.commit()

    @close_session
    def is_like(self, usid, acid):
        """是否点赞"""
        return self.session.query(ActivityLike).filter_by(USid=usid, ACid=acid).first()

    @close_session
    def del_like(self, usid, acid):
        """删除点赞"""
        return self.session.query(ActivityLike).filter_by(USid=usid, ACid=acid).delete()

    @close_session
    def cancel_like_by_acid(self, acid):
        """取消点赞"""
        cur_activity = self.session.query(Activity).filter_by(ACid=acid).first()
        if cur_activity.AClikeFakeNum:
            cur_activity.AClikeFakeNum -= 1
        else:
            cur_activity.AClikenum -= 1
        self.session.add(cur_activity)
        # self.session.commit()
        # return self.session.query(Activity).filter(Activity.ACid == acid).update({
        #     'AClikeFakeNum': Activity.AClikeFakeNum - 1,
        #     'AClikenum': Activity.AClikenum - 1
        # })
