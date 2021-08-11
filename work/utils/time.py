# -*- coding: utf-8 -*-
# 时间解析类
# 作者: 三石
# 时间: 2020-04-13

import time
from datetime import datetime
from work.utils import UtilsLog


class UtilsTime:
    def __init__(self):
        self.logger = UtilsLog()
        self.logger.info("调用时间解析类")
        self.logger.info(self.__class__)

    def get_datetime_str(self, date_time):
        """
        时间格式转格式
        :param date_time: date_time格式数据
        :return:
        """
        self.logger.info("date_time: {}".format(date_time))
        date_time_str = datetime.strftime(date_time, "%Y-%m-%d %H:%M:%S")
        self.logger.info("返回数据: {}".format(date_time_str))
        self.logger.info(date_time_str)
        return date_time_str
