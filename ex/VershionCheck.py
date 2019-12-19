#-*- coding:utf-8 -*-

def compare(a, b):
    la = a.split('.')
    lb = b.split('.')
    f = 0
    #判断ab长度
    if len(la) > len(lb):
        f = len(la)
    else:
        f = len(lb)
    
    for i in range(f):
        try:
            if int(la[i]) > int(lb[i]):
                print(a + '>' + b)
                return
            elif int(la[i]) == int(lb[i]):
                continue
            else:
                print(a + '<' + b)
                return
        except:
#             if len(la) > len(lb):
#                 print(a + '>' + b)
#                 return
#             else:
#                 print(a + '<' + b)
#                 return
            print("版本号格式错误")
            return
            
    print(a + '=' + b)

if __name__ == "__main__":
    a = "1.101"
    b = "1.101.1"
    compare(a,b)
    