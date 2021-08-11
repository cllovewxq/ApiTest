# -*- coding: utf-8 -*-
# 日志工具类
# 作者: 三石
# 时间: 2021-08-02

import logging


class UtilsLog:
    def __init__(self):
        """日志工具类"""
        self.logger = logging.getLogger(__name__)
        # 日志格式
        self.log_format = "%(asctime)s - %(levelname)s - %(message)s"
        self.log_date_format = "%Y-%m-%d %H:%M:%S"
        logging.basicConfig(format=self.log_format, datefmt=self.log_date_format, level=logging.DEBUG)

    def info(self, message):
        return self.logger.info(message)

    def debug(self, message):
        return self.logger.debug(message)

    def warning(self, message):
        return self.logger.warning(message)

    def error(self, message):
        return self.logger.error(message)
