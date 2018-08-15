# *- coding:utf8 *-
import sys
import os
from collections import namedtuple

sys.path.append(os.path.dirname(os.getcwd()))
from SBase import SBase, close_session
from WeiDian.models.model import ActivityMedia, Activity
media = namedtuple('media', ['ACid', 'AMmedia', 'AMsort'])


class SActivityMedia(SBase):

    @close_session
    def get_media_by_acid(self, acid):
        """获取活动中的媒体信息
        如果是视频, 返回一个单视频列表
        如果是图片, 返回图片列表"""
        cur_medias = self.session.query(ActivityMedia).filter_by(ACid=acid)
        if cur_medias.count == 1 and cur_medias.first().AMvideo:
            cur_media = cur_medias.first()
            return [media(cur_media.AMid, cur_media.AMvideo, cur_media.AMsort), ]
        else:
            return [media(cur_media.AMid, cur_media.AMimage, cur_media.AMsort) for cur_media in cur_medias]





