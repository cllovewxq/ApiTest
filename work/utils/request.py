# -*- coding: utf-8 -*-
# 请求工具类
# 作者: 三石
# 时间: 2019-10-21

import requests
from work.utils import UtilsLog
from requests.exceptions import ConnectTimeout, ReadTimeout, ConnectionError, RequestException


class UtilsRequest:
    def __init__(self):
        """请求工具类"""
        self.logger = UtilsLog()
        self.logger.info("调用请求工具类")
        self.logger.info(self.__class__)

        self.session = requests.Session()

        self.timeout = 5

        self.api = requests

    def post(self, url, headers=None, params=None, json=None, data=None, files=None):
        """
        Post请求方法
        :param url: 请求地址
        :param headers: 请求头
        :param params: 请求头参数
        :param json: 请求JSON参数
        :param data: 请求DATA参数
        :param files: 请求FILE参数
        :return:
        """
        self.logger.debug("接口请求headers:")
        self.logger.debug(str(headers).replace('\'', '\"'))
        self.logger.debug("接口请求params:")
        self.logger.debug(str(params).replace('\'', '\"'))
        self.logger.debug("接口请求json:")
        self.logger.debug(str(json).replace('\'', '\"'))
        self.logger.debug("接口请求data:")
        self.logger.debug(str(data).replace('\'', '\"'))
        self.logger.debug("接口请求files:")
        self.logger.debug(files)
        try:
            response = self.api.post(url=url, headers=headers, params=params, json=json, data=data, files=files, timeout=self.timeout, verify=False)
            code = response.status_code
            text = response.text
            self.logger.info("接口请求返回状态码: {}".format(code))
            self.logger.info(text)
            return text
        except ConnectTimeout:
            self.logger.error("接口连接超时!")
            return False
        except ReadTimeout:
            self.logger.error("接口请求超时!")
            return False
        except ConnectionError:
            self.logger.error("接口请求错误!")
            return False
        except RequestException:
            self.logger.error("接口请求返回错误!")
            return False

    def get(self, url, headers=None, params=None):
        """
        Get请求方法
        :param url: 请求地址
        :param headers: 请求头
        :param params: 请求头参数
        :return:
        """
        self.logger.debug("接口请求headers:")
        self.logger.debug(str(headers).replace('\'', '\"'))
        self.logger.debug("接口请求params:")
        self.logger.debug(str(params).replace('\'', '\"'))
        try:
            response = self.api.get(url=url, headers=headers, params=params, timeout=self.timeout, verify=False)
            code = response.status_code
            text = response.text
            self.logger.info("接口请求返回状态码: {}".format(code))
            self.logger.info(text)
            return text
        except ConnectTimeout:
            self.logger.error("接口连接超时!")
            return False
        except ReadTimeout:
            self.logger.error("接口请求超时!")
            return False
        except ConnectionError:
            self.logger.error("接口请求错误!")
            return False
        except RequestException:
            self.logger.error("接口请求返回错误!")
            return False
