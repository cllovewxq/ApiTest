# -*- coding: utf-8 -*-
# 检查类
# 作者: 三石
# 时间: 2021-06-03

from work.utils import UtilsLog
from work.utils import UtilsResponse
from datetime import datetime
import allure
import json


class UtilsCheck:
    def __init__(self):
        self.logger = UtilsLog()
        self.logger.info("调用Allure检查类")
        self.logger.info(self.__class__)

    @allure.step("基础校验返回值")
    def check_key_value_base(self, _json, _key, _value):
        """
        基础校验返回值
        :param _json: 返回信息
        :param _key: 键值
        :param _value: 期望值
        :return: True或者False
        """
        value = UtilsResponse().get_key_value(_json=_json, _key=_key)
        assert value == _value

    @allure.step("通用校验返回值")
    def check_key_value_common(self, _json, _key, _value, is_list=True, is_equal=True, is_case_insensitive=True):
        """
        通用校验返回值
        :param _json: 返回信息
        :param _key: 键值
        :param _value: 期望值
        :param is_list: 返回json是否列表 默认是
        :param is_equal: 校验规则是否相等 默认是
        :param is_case_insensitive: 是否不区分大小写 默认是
        :return: True或者False
        """
        # 是列表
        if is_list:
            assert _json != []
            for x, y in enumerate(_json):
                # 相等
                if is_equal:
                    assert y[_key] == _value
                # 模糊匹配
                else:
                    # 判断是否不区分大小写
                    if is_case_insensitive:
                        assert _value in y[_key]
                    else:
                        assert _value.lower() in y[_key].lower()
        # 不是列表
        else:
            # 相等
            if is_equal:
                assert _json[_key] == _value
            # 模糊匹配
            else:
                # 判断是否不区分大小写
                if is_case_insensitive:
                    assert _value in _json[_key]
                else:
                    assert _value.lower() in _json[_key].lower()

    @allure.step("校验返回列表")
    def check_key_value_list(self, _json, _key, _values, num):
        """
        校验返回列表
        :param _json: 返回信息
        :param _key: 键值
        :param _values: 期望列表
        :param num: 期望数量
        :return:
        """
        assert len(_json) == num
        values = []
        for x, y in enumerate(_json):
            values.append(y[_key])
        self.logger.debug("期望数据:")
        self.logger.debug(_values)
        self.logger.debug("实际数据:")
        self.logger.debug(values)

        for x, y in enumerate(_values):
            assert y in _values
        for x, y in enumerate(values):
            assert y in values

    @allure.step("校验返回值排序")
    def check_key_sort(self, _json, _key, _is_desc=True):
        """
        校验返回值排序
        :param _json: 返回信息
        :param _key: 键值
        :param _is_desc: 是否倒序
        :return: True或者False
        """
        if _is_desc:
            start = float("inf")
            for x, y in enumerate(_json):
                assert start >= y[_key]
                start = y[_key]
        else:
            start = float("-inf")
            for x, y in enumerate(_json):
                assert start <= y[_key]
                start = y[_key]

    @allure.step("校验时间返回值排序")
    def check_key_time_sort(self, _json, _key, _is_desc=True):
        """
        校验时间返回值排序
        :param _json: 返回信息
        :param _key: 键值
        :param _is_desc: 是否倒序
        :return: True或者False
        """
        if _is_desc:
            start = float("inf")
            for x, y in enumerate(_json):
                timestamp = datetime.timestamp(datetime.strptime(y[_key], "%Y-%m-%d %H:%M:%S"))
                assert start >= timestamp
                start = timestamp
        else:
            start = float("-inf")
            for x, y in enumerate(_json):
                timestamp = datetime.timestamp(datetime.strptime(y[_key], "%Y-%m-%d %H:%M:%S"))
                assert start <= timestamp
                start = timestamp

    @allure.step("校验返回值是否存在")
    def check_key_is_extend(self, _json, _key):
        """
        校验返回值是否存在
        :param _json: 返回信息
        :param _key: 键值
        :return: True或者False
        """
        if type(_json) == str:
            return _key in json.loads(_json).keys()
        return _key in _json.keys()
