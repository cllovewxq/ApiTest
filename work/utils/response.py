# -*- coding: utf-8 -*-
# 返回解析工具类
# 作者: 三石
# 时间: 2019-10-21

import json
from work.utils import UtilsLog


class UtilsResponse:
    def __init__(self):
        """调用返回解析工具类"""
        self.logger = UtilsLog()
        self.logger.info("调用基础返回解析工具类")
        self.logger.info(self.__class__)

    def get_key_value(self, _json, _key):
        """
        :param _json: 返回信息
        :param _key: key键值 层级用 . 来间隔
        :return: 返回value
        """
        self.logger.debug("开始解析返回信息: {}, key: {}".format(_json, _key))
        try:
            key_list = _key.split(".")

            value = json.loads(_json)
            for key in key_list:
                value = value[key]

            self.logger.debug("成功解析: {}".format(value))
            return value
        except KeyError as error:
            self.logger.error("json解析出错缺少Key:")
            self.logger.error(error)
            return error


