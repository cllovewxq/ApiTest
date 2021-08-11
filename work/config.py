# -*- coding: utf-8 -*-
# 项目配置信息
# 作者: 三石
# 时间: 2021-06-02

import os


class WorkConfig:
    def __init__(self):
        """
        项目配置信息
        """
        # 项目路径
        self.base_path = os.path.abspath(os.path.dirname(__file__))

        self.files_path = self.base_path + "/files"

    @property
    def files_yaml_path(self):
        """
        yaml文件路径
        :return:
        """
        return self.files_path + "/files_yaml/"

    @property
    def files_rsa_path(self):
        """
        RSA加密文件路径
        :return:
        """
        return self.files_path + "/files_rsa/"

    @property
    def files_xml_path(self):
        """
        xml文件路径
        :return:
        """
        return self.files_path + "/files_xml/"

    @property
    def files_txt_path(self):
        """
        txt文件路径
        :return:
        """
        return self.files_path + "/files_txt/"

    @property
    def files_image_path(self):
        """
        image文件路径
        :return:
        """
        return self.files_path + "/files_image/"

    @property
    def files_excel_path(self):
        """
        excel文件路径
        :return:
        """
        return self.files_path + "/files_excel/"

    @property
    def reports_path(self):
        """
        报告文件路径
        :return:
        """
        return self.base_path + "/reports"

    @property
    def cases_path(self):
        """
        用例文件路径
        :return:
        """
        return self.base_path + "/cases"
