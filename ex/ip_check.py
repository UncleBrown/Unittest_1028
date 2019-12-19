#!/usr/bin/python3
#-*- coding:utf-8 -*-
import re

def checkIP(info):
    list1 = info.split(".")
    result = None
    
    if len(list1)== 4:
        print(list1)
        print("4位IP地址\n")
        
        for i in list1:
            #对IP第一位进行判断
            if i == list1[0]:
                #如果格式为1-9|10~19|100~199|200~249|250~255
                if re.findall('^[0][0][1-9]$|^[0][1][0-9]$|^[1][0-9][0-9]$|^[2][0-4][0-9]$|^[2][5][0-5]$',i):
                #if re.findall('',i)
                    print(i + " 合格")
                    result = True
                    continue
                else:
                    result = False
                    print(i + "不合格")
                    return result
            #如果i不等于list1[0]即i不是ip第一位，
            if re.findall('^[0][0][0-9]$|^[0][1][0-9]$|^[1][0-9][0-9]$|^[2][0-4][0-9]$|^[2][5][0-5]$',i):
                print(i + ' 符合')
            else:
                result = False
                print(i + ' 不符合')
                return result
    else:
        result = False
        print(list1)
        print('不符合IP地址规范')
    return result

if __name__ == "__main__":
    a = "ab.168.131.200"
    if checkIP(a):
        print("此IP符合规则")
    else:
        print("此IP不符合规则")
            