#!/usr/bin/python3
#-*- coding:utf-8 -*-

import re 

def checkIP(IP):
    
    listIP = IP.split(".")
    
    
    if len(listIP) != 4:
        print("IP 长度错误\n")
        return False
    
    for i in range(4):
       
        try:
            #判断每个元素是不是数字
            listIP[i] = int(listIP[i])
        except:
            print(f"IP元素类型错误:{i}\n")
            return False
        
        if listIP[i] <= 255 and listIP[i]>= 1:
            #print(type(listIP[i]))
            print(str(listIP[i]) + " 合格")
        else:
            print(f"IP元素数值过大或过小:{listIP[i]}")
            return False
    
    #for 循环执行完毕，没有异常则return True
    return True
if __name__ == "__main__":
    ip = "256.158.131.118"
    if checkIP(ip):
        print("ip 符合")
    else:
        print("ip 不符合")
               
    
            
            