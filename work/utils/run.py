# -*- coding: utf-8 -*-
# 运行工具类
# 作者: 三石
# 时间: 2021-05-31

import sys
import getopt
import pytest
import os

from work.utils import UtilsLog
from work.config import WorkConfig
from datetime import datetime


class UtilsRun:
    def __init__(self):
        """
        运行工具类
        """
        self.logger = UtilsLog()
        self.logger.info("调用运行工具类")
        self.logger.info(self.__class__)

        self.cases_path = WorkConfig().cases_path
        self.report_path = WorkConfig().reports_path

        self.file_results = "allure-results"
        self.file_report = "allure-report"

    def create_path(self, path):
        """
        创建文件夹
        :param path: 文件路径名称
        :return:
        """
        self.logger.info("创建文件夹")
        if os.path.exists(path):
            pass
        else:
            os.makedirs(path)

    def init_files(self, cases_name, version):
        """
        初始化文件夹
        :param cases_name: 测试用例文件路径名称
        :param version: 版本 默认Test
        :return:
        """
        self.logger.debug("初始化文件路径......")

        # 判断是否创建报告路径
        self.create_path(self.report_path)

        # 创建测试报告文件目录
        # 非Jenkins模式
        # 根据时间创建
        if version != "Jenkins":
            path = "{base}/{version}/{cases}/{time}/{file}"
            run_time = datetime.today().strftime("%Y%m%d%H%M%S")

            # 修改 file_results, file_report
            self.file_results = path.format(base=self.report_path, version=version, cases=cases_name[1:].replace("\\", "-"), time=run_time, file=self.file_results)
            self.file_report = path.format(base=self.report_path, version=version, cases=cases_name[1:].replace("\\", "-"), time=run_time, file=self.file_report)

        # Jenkins模式
        # Jenkins配置中填写此结果路径 file_results
        # Jenkins配置中填写此报告路径 file_report
        else:
            path = "{base}/Jenkins/{cases}/{file}"

            # 修改 file_results, file_report
            self.file_results = path.format(base=self.report_path, cases=cases_name[1:].replace("\\", "-"), file=self.file_results)
            self.file_report = path.format(base=self.report_path, cases=cases_name[1:].replace("\\", "-"), file=self.file_report)

        # 初始化文件夹
        self.create_path(self.file_results)
        self.create_path(self.file_report)

    def run_pytest(self, cases_name):
        """
        运行pytest
        :param cases_name: 测试用例文件路径名称
        :return:
        """
        self.logger.info("=================================================")
        self.logger.debug("开始执行自动化测试用例......")
        self.logger.debug("打开测试用例路径......")

        self.logger.info("运行测试文件......")
        # 执行并指定结果路径
        pytest.main(["-q", "-s", "--alluredir=" + self.file_results, self.cases_path + cases_name,
                     "--clean-alluredir",
                     "--log-date-format=%Y-%m-%d %H:%M:%S",
                     "--log-format=%(asctime)s - %(message)s"])
        self.logger.info("运行结束......")

    def run_xml(self):
        """
        生成测试报告
        :return:
        """
        self.logger.info("生成测试报告......")
        # 根据指定结果路径生成报告
        cmd = "allure generate " + self.file_results + " -o " + self.file_report + " --clean"
        os.system(cmd)
        self.logger.info("生成结束......")
        self.logger.info("=================================================")

    def help(self):
        """
        帮助信息
        :return:
        """
        self.logger.debug("帮助信息:")
        self.logger.debug(" *  -h : 帮助信息")
        self.logger.debug(" *  -v [val] : 版本号 ps: -v V1.0")
        self.logger.debug(" *  -p [val] : 测试路径 ps: -p /argus")

    def init_run(self):
        """
        初始化
        :return:
        """
        self.logger.debug("运行用例执行参数模式......")
        version = None
        path = None
        try:
            opts, args = getopt.getopt(sys.argv[1:], "hv:e:p:")
            for op, value in opts:
                if op == "-v":
                    version = value
                elif op == "-p":
                    path = value.replace("/", "\\")
                    # path = value
                elif op == "-h":
                    # 打印帮助信息
                    self.help()
                    # 退出
                    sys.exit()
                else:
                    sys.exit()
        except getopt.GetoptError as e:
            self.logger.error("出现ERROR:")
            self.logger.error(e)

        if version is None or path is None:
            self.logger.info("运行参数解析失败,请重新输入参数!")
            self.logger.info("可以输入 -h,获取帮助信息!")
            # 退出
            sys.exit()

        _json = {
            "version": version,
            "path": path
        }
        return path, version

    def run_main(self):
        """
        运行主函数
        :return:
        """
        # 初始化读取 case文件夹 版本
        cases_name, version = self.init_run()
        # 初始化文件夹
        self.init_files(cases_name=cases_name, version=version)
        # 运行+生成报告
        self.run_pytest(cases_name=cases_name)
        self.run_xml()
