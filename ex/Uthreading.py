#!/usr/bin/python3
#-*- coding:utf-8 -*-

import threading

def action(max):
    for i in range(max):
        #current_thread():获取当前线程
        #getName():获取当前线程名
        print(threading.current_thread().getName() + " " + str(i))
    
for i in range(100):
    print(threading.current_thread().getName() + " " + str(i))
    
    if i == 20:
        t1 = threading.Thread(target=action,args=(100,))
        t1.start()
        t2 = threading.Thread(target=action,args=(100,))
        t2.start()
print('主线程执行完成！')