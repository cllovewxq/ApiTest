# -*- coding: utf-8 -*-
# 随机工具类
# 作者: 三石
# 时间: 2021-07-09


import random
from work.utils import UtilsLog


class UtilsRandom(object):
    def __init__(self):
        """
        转换工具类
        """
        self.logger = UtilsLog()

    @property
    def random_list(self):
        num_list = []

        # 数字0-9
        for x in range(0, 10):
            num_list.append(x)

        # 大写字母
        for x in range(65, 91):
            num_list.append(chr(x))

        # 小写字母
        for x in range(97, 123):
            num_list.append(chr(x))

        return num_list

    def get_random_code(self, num=6):
        """
        随机生成验证码
        :param num: 验证码位数 默认6位
        :return:
        """
        self.logger.info("随机生成验证码: {}位".format(num))
        code_list = []
        for i in range(num):
            random_num = random.choice(self.random_list)
            code_list.append(str(random_num))

        random_code = ''.join(code_list)
        return random_code
