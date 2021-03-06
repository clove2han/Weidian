# -*- coding: utf-8 -*-
from datetime import datetime

from WeiDian.common.timeformat import format_for_db
from WeiDian.models.model import PartnerSellOrInviteMatch, PartnerSellOrinviteMount, User
from WeiDian.service.SBase import SBase, close_session


class SPartnerSellOrInviteMatch(SBase):
    @close_session
    def get_lasting_partner_match(self, level, closed=False):
        """指定等级的正在进行中的邀请或销售额活动"""
        time_now = datetime.strftime(datetime.now(), format_for_db)
        return self.session.query(PartnerSellOrInviteMatch).filter(
            PartnerSellOrInviteMatch.PSIMstarttime < time_now,
            PartnerSellOrInviteMatch.PSIMendtime > time_now,
            # PartnerSellOrInviteMatch.PSIMlevel == level,
            PartnerSellOrInviteMatch.PSIMisclose == closed
        ).first()

    @close_session
    def update_partner_match(self, level, data):
        """指定等级的正在进行中的邀请或销售额活动"""
        time_now = datetime.strftime(datetime.now(), format_for_db)
        return self.session.query(PartnerSellOrInviteMatch).filter(
            PartnerSellOrInviteMatch.PSIMstarttime < time_now,
            PartnerSellOrInviteMatch.PSIMendtime > time_now,

            # PartnerSellOrInviteMatch.PSIMlevel == level,
        ).update(data)

    @close_session
    def update_partner_match_by_psmid(self, psmid, data):
        """更新"""
        return self.session.query(PartnerSellOrInviteMatch).filter(PartnerSellOrInviteMatch.PSIMid == psmid).update(data)

    @close_session
    def get_partner_match_mount_by_usidpsmid(self, usid, psimid):
        """获取合伙人的活动状态"""
        return self.session.query(PartnerSellOrinviteMount).filter(
            PartnerSellOrinviteMount.PSIMid == psimid,
            PartnerSellOrinviteMount.USid == usid
        ).first()

    @close_session
    def update_partner_match_mount_by_psomid(self, psomid):
        """更新参加活动的数据"""
        return self.session.query(PartnerSellOrinviteMount).filter(
            PartnerSellOrinviteMount.PSOMid == psomid,
        ).first()

    @close_session
    def get_partner_match_mount_gt_value(self, psimid, value):
        """大于该活动中某值合伙人成绩人数"""
        return self.session.query(PartnerSellOrinviteMount).filter(
            PartnerSellOrinviteMount.sellorinvitemount > value,
            PartnerSellOrinviteMount.PSIMid == psimid
        ).count()

    @close_session
    def get_partner_match_mount_gt_value_in_currentlevel(self, psimid, value, level):
        return self.session.query(PartnerSellOrinviteMount).\
            join(User, User.USlevel == level).filter(
            PartnerSellOrinviteMount.sellorinvitemount > value,
            PartnerSellOrinviteMount.PSIMid == psimid,
            User.USlevel == level
        ).count()


