#!/usr/bin/python3
#-*- coding:utf-8

import requests
import json

class RunMethod():
     
    def __ini__(self):
        pass
     
    def run_get(self,url,data,header):
        if header:
            r = requests.get(url=url,data=data,headers=json.loads(header)).json()
        else:
            r = requests.get(url=url,data=data).json()
        return json.dumps(r,indent=4)
        
     
    def run_post(self,url,data,header):
        #print(f"header:{header}")
        if header:
            r = requests.post(url=url,json=data,headers=json.loads(header)).json() #将header字符串（json）转换成dict
        else:
            r = requests.post(url=url,data=data).json()
        return json.dumps(r,indent=4)
     
    def run_main(self,method,url,data,header):

        #print(f"method:{method}")
        #print(f"method:{method.lower()}")
        
        if method.lower() == "get":
            r = self.run_get(url,data,header)
        elif method.lower() == "post":
            r = self.run_post(url,data,header)
            return r
        else:
            print("[info]:Case Method error ...")
        
if __name__ == "__main__":
    
    method = ""
    url = ""
    data = ""
    header = ""
    
    re_requests = RunMethod()
    re_requests.run_main(method,url,data,header)
        