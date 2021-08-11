# -*- coding: utf-8 -*-
# yaml文件解析类
# 作者: 三石
# 时间: 2019-10-21

import yaml
import os

from work.utils import UtilsLog
from work.config import WorkConfig


class UtilsYaml:
    def __init__(self, filename):
        """yaml文件解析类"""
        self.logger = UtilsLog()
        self.logger.info("调用配置文件yaml解析类")
        self.logger.info(self.__class__)

        self.filename = filename

    def read(self):
        """读取"""
        self.logger.debug("打开yaml文件")
        yaml_file = os.path.join(WorkConfig().files_yaml_path + self.filename)
        self.logger.debug(yaml_file)
        with open(yaml_file, "rb") as f:
            info = f.read()
        # yaml版本优化
        r_info = yaml.load(info, Loader=yaml.FullLoader)
        self.logger.debug("成功解析yaml文件...")
        self.logger.debug(r_info)
        return r_info
