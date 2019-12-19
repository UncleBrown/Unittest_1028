#!/usr/bin/python3
#-*- coding:utf-8 -*-

import unittest
from case import unittest_text
import HTMLTestRunner
#import json
import time
import os


suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromModule(unittest_text))
#suite.addTest(TestMethod('test_1'))
#unittest.TextTestRunner().run(suite)
now = time.strftime('%Y-%m-%d %H%M%S')
fp_path = "log/" #路径设置方式可以参考linux
#filename = open(os.getcwd() + '/log/testResult_Report_' + now + '.html','wb')
filename = open(fp_path + 'testResult_Report_' + now + '.html','wb')
runner = HTMLTestRunner.HTMLTestRunner(
    stream=filename,
    title='接口测试报告',
    description='接口测试报告',
    verbosity = 2)
runner.run(suite)
filename.close()