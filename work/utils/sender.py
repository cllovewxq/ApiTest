# -*- coding: utf-8 -*-
# sender工具类
# 作者: 三石
# 时间: 2021-07-01

import socket
import struct
import json
import time
from work.utils import UtilsLog


class UtilsSender(object):

    def __init__(self, server_host, server_port):
        """
        sender工具类
        :param server_host: 服务地址ip
        :param server_port: 服务端口号
        """
        self.logger = UtilsLog()
        self.server_host = server_host
        self.server_port = server_port

        self.header_protocol = "ZBXD"

        self.request = ""
        self.response = ""

        self.data = []

    @property
    def header(self):
        """
        信息头
        :return:
        """
        flags = "\1"
        header = (self.header_protocol + flags).encode("utf-8")
        return header

    def get_request_packet(self):
        """
        请求包
        :return:
        """
        packet = {
            "request": "sender data",
            "data": self.data
        }
        # json转str
        packet = json.dumps(packet, ensure_ascii=False).encode("utf-8")

        packet_len = struct.pack("<Q", len(packet))

        # 拼接
        request_packet = self.header + packet_len + packet
        return request_packet

    def send(self, packet):
        """
        发送
        :param packet: 请求包
        :return:
        """
        self.logger.info("开始连接socket...")
        self.logger.info("数据包: {}".format(packet))

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # 设置超时
            sock.settimeout(5)
            sock.connect((self.server_host, self.server_port))

            self.logger.info("连接成功,开始发送数据包")
            # 发送请求
            sock.sendall(packet)

            # 获取返回头
            response_header = sock.recv(13)

            packet_len = struct.unpack("<Q", response_header[len(self.header):])[0]
            response_packet = sock.recv(packet_len)

            self.logger.info("返回数据包：{}".format(response_packet))
            sock.close()

            # 获取socket返回包里的info字段 并去除空格
            info = json.loads(response_packet)["info"].replace(" ", "")

            # 拼接info组装detail
            detail = {}
            for item in info.split(";"):
                group = item.split(":")
                detail[group[0]] = group[1]

            self.logger.info("返回信息：{}".format(detail))
            self.response = {
                "response": "success",
                "detail": detail,
            }

        # 拦截异常
        except socket.timeout as e:
            sock.close()
            self.logger.error("出现异常,异常信息：{}".format(e))

            self.response = {
                "response": "error",
                "detail": e,
            }

        except OSError as e:
            sock.close()
            self.logger.error("出现异常,异常信息：{}".format(e))

            self.response = {
                "response": "error",
                "detail": e,
            }

        except Exception as e:
            sock.close()
            self.logger.error("出现异常,异常信息：{}".format(e))

            self.response = {
                "response": "error",
                "detail": e,
            }

    def init_data(self):
        """
        初始化data
        :return:
        """
        self.logger.info("初始化Data")
        self.data = []

    def insert_obj(self, host, key, value, clock=None):
        """
        新增数据源
        :param host: 主机名称
        :param key: 监控项key
        :param value: 监控项值
        :param clock: 时间戳
        :return:
        """
        if clock is None:
            clock = self.clock

        obj = {
            "host": str(host),
            "key": key,
            "value": value,
            "clock": clock,
        }
        self.logger.info("新增数据：{}".format(obj))
        self.data.append(obj)

    @property
    def clock(self):
        """
        当前时间戳
        :return:
        """
        return int(time.time())
