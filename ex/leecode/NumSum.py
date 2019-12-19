#-*_ coding:utf-8 -*-
'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标
'''

def two_num(nums,target):
    
    dct={}
    
    #enumerate()将可遍历数据对象（列表，元祖或字符串）组合为一个索引序列，同时列出索引和数据下标，一般用在循环中
    #print(list(enumerate(nums)))
    for i,n in list(enumerate(nums)):
        if target - n in dct:
            return [dct[target -n],i]
        dct[n] = i
        print(dct)
    
    print(dct)
    
if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    two_num(nums,target)