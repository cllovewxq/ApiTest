# -*- coding: utf-8 -*-
# 运行入口
# 作者: 三石
# 时间: 2021-05-31


from work.utils import UtilsRun, UtilsLog


if __name__ == '__main__':
    logger = UtilsLog()
    logger.debug("开始运行API接口自动化测试...")
    run = UtilsRun()
    run.run_main()
    logger.debug("结束运行API接口自动化测试...")
