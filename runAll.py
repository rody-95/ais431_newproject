# -*- coding: utf-8 -*-
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from logging import *
if __name__ == "__main__":
    # 定义测试用例的存放路径
    test_dir = "./testCases/"
    # 把测试用例加入 discover 容器
    discover = unittest.defaultTestLoader.discover(test_dir, "*.py")

    # 定义测试报告的存放路径
    testReportDir = "./reports/"
    # 定义测试报告的名字
    nowTime = time.strftime("%Y-%m-%d%H%M%S", time.localtime())
    fileName = nowTime + ".html"
    # 测试报告路径名字
    testReportDir_FileName = testReportDir + fileName

    # 打开文件，并赋予可写权限
    fp = open(testReportDir_FileName, "wb")

    # 把测试结果写进测试报告，并装载到HTHMLTestRunner模块
    runner = HTMLTestRunner(stream=fp, title="接口自动化测试报告", description="接口用例执行情况")

    # 运行测试用例
    runner.run(discover)
    fp.close()  # 关闭文件
