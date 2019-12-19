#!/usr/bin/python3
#-*- coding:utf-8 -*-

import requests
import json

class RunMain():
    
    #def __ini__(self,url,method,data=None,headers=None):#实例化后自动调用
    #    self.res = self.run_main(url, method,data,headers)
    
    def send_get(self,url,data,headers):
        res = requests.get(url=url,data=data,headers=headers).json()
        #r.json()为requests内置json解码器，如果r返回不是json格式，则r.json()会报错
        #将json转换成dict
        #return json.dumps(res,indent=2,sort_keys=True)
        return res
    def send_post(self,url,data,headers):
        res = requests.post(url=url,data=data,headers=headers).json()
        #return json.dumps(res,indent=2,sort_keys=True)
        return res
        
    def run_main(self,url,method,data=None,headers=None):
        res = None
        if method.lower() == "get":
            res = self.send_get(url,data,headers)
        elif method.lower() == "post":
            res = self.send_post(url,data,headers)
        else:
            print("[info]:Method Err,Please Check")
        return res
        
if __name__ == "__main__":
    
#     url = "http://192.168.131.118:10001/mis/statistics"
#     data = {
#         "site_info": [
#             {
#             "site_id": 7, 
#             "push_sum": 2000
#             }]
#         }
        
    url = "http://192.168.131.118:10001/vmis/statistics"
    data = {
        "site_info": [
            {
            "site_id": 7, 
            "push_sum": 2000
            }]
        }
    run = RunMain()
    res = run.run_main(url,"Post",data=json.dumps(data)) #将data对象（字典）序列化为字节流格式
    #result = json.loads(res.content)
    print(res)