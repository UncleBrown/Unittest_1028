#/usr/bin/python3
#-*- coding:utf-8 -*-

def bubbleSort(arr):
    n = len(arr)
    #print(f"n:{n}\n")
    for i in range(n):
        print("\n"+"="*30)
        print(f"i:{i}\n")
        for j in range(n-i-1):
            print(f"j:{j}")
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        #return arr
    
if __name__ == "__main__":
    sortList = [64, 34, 25, 12, 22, 11, 90]
    bubbleSort(sortList)
    