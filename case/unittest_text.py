#!/usr/bin/python3
#-*- coding:utf-8 -*-

import unittest
from lib.base import RunMain
import HTMLTestRunner
import json
import time
import os
from case import unittest_text

class TestMethod(unittest.TestCase):
        
    @classmethod#装饰器，配合setUpClass/tearDownClass使用，使之不必再每条用例前后均执行，减少代码量
    def setUpClass(self):
        print("setUp")
    
    @classmethod
    def tearDownClass(self):
        print("tearDown")

    def test_1(self):
        
        url = "http://192.168.131.118:10001/vmis/statistics"
        data = {
            "site_info": [
                {
                "site_id": 7, 
                "push_sum": 2000
                }]
            }
        
        res = RunMain().run_main(url,"Post",data=json.dumps(data))
        #.encode('utf-8').decode('unicode_escape')
        #将unicode字符串，编码为utf-8的bytes格式，在解码为字符串
        print(res)
        #self.assertEqual(res['retcode'],'200')
        
    def test_2(self):
        
        url = "http://192.168.131.118:10001/vmis/statistics"
        data = {
            "site_info": [
                {
                "site_id": 7, 
                "push_sum": 2000
                }]
            }
        
        res = RunMain().run_main(url,"Post",data=json.dumps(data))
        #.encode('utf-8').decode('unicode_escape')
        #将unicode字符串，编码为utf-8的bytes格式，在解码为字符串
        #print("222")
        self.assertEqual(res['retcode'],'200')
        
if __name__ == "__main__":
    #unittest.main()
#     suite = unittest.TestSuite()
#     suite.addTest(TestMethod('test_2'))
#     suite.addTest(TestMethod('test_1'))
    #suite = unittest.TestLoader().loadTestsFromModule(unittest_text) #从moudle加载测试用例
    suite = unittest.TestLoader().loadTestsFromName('unittest_text.TestMethod.test_1') #格式：moudle--class--method，字符串
    #suite = unittest.defaultTestLoader.discover('../case',pattern='unittest_text.py')
    runner = unittest.TextTestRunner(verbosity=2) #参数表示显示结果信息复杂度
    runner.run(suite)
    