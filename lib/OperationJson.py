#!/usr/bin/python3 
#-*- coding:utf-8

import json

class OperationJson():
    
    def __init__(self,jsonfile=None):
        if jsonfile:
            self.jsonflie = jsonfile
        else:
            self.jsonflie = "../case/rdata.json"
        #self.jsonflie = jsonfile
        #self.id = json_id
        self.data = self.read_data()
    
    #读取Json文件
    def read_data(self):
        with open(self.jsonflie,encoding='utf-8') as fp:
            #print(fp)
            #加载json文件，多行会报错
            data = json.load(fp)
            #print(data)
            return data
    
    #根据关键字获取数据
    def get_json_data(self,id):
        return self.data[id]
        #return self.read_data()[self.id]
    
if __name__ == "__main__":
    fjson = "../case/rdata.json"
    opjson = OperationJson(fjson)
    print(opjson.get_json_data("site_info_2"))
        
            