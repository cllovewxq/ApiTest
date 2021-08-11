# -*- coding: utf-8 -*-
# demo测试用例
# 作者: 三石
# 时间: 2021-08-11

from work.utils import UtilsLog, UtilsCheck, UtilsRsa, UtilsDB, UtilsResponse, UtilsRequest, UtilsRandom
import allure
import pytest


@allure.feature("测试模块：设备组创建")
class TestDemo:

    @classmethod
    def setup_class(cls):
        cls.logger = UtilsLog()
        cls.logger.debug("开始执行测试类 .......")

    @classmethod
    def teardown_class(cls):
        cls.logger.debug("结束执行测试类.......")

    def setup_method(self):
        self.logger.debug("测试用例执行开始...")

    def teardown_method(self):
        self.logger.debug("测试用例执行结束...")

    @allure.story("测试用例-demo")
    def test_demo_01(self):
        req = UtilsRequest()
        resp = req.post(url="http://xx.xx.xx/xxx", json={
            "username": "XXX",
            "password": "XXX"
        })

        UtilsCheck().check_key_value_base(_json=resp, _key="code", _value="200")
        UtilsCheck().check_key_value_base(_json=resp, _key="success", _value=False)
        UtilsCheck().check_key_value_base(_json=resp, _key="message", _value="XXX")
        UtilsCheck().check_key_value_base(_json=resp, _key="data", _value=[])

