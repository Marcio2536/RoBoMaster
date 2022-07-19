from ast import Pass
import re
import random
from unittest import result
enter=input("Enter 4 number and a sign")
sign=enter[4]
ele=[]
enter_list=[0,0,0,0]
reslt=0
solution=""
len=0
def analyze():
    global len
    for i in range(4):
        enter_list[i]=enter[i]
    for i in range(4):
        for j in range(4):
            enter_list.append(str(enter_list[i])+str(enter_list[j]))
    len=len(enter_list)
    for i in range(len):
        enter_list[i]=int(enter_list[i])
    if sign=="+":
        pass
        #plus()
    elif sign=="-":
        pass
        #minus()
    elif sign=="*":
        pass
        #multi()
    else:
        pass
        #divid()
def plus():
    plist=enter_list
    len=len(plist)
    plist.sort(reverse=True)
    for i in range(len):
        if plist[i]>24:
            del plist[i]
        for j in range(len):
            reslt=plist[i]+plist[j]
            if reslt==24:
                solution=str(i)+"+"+str(j)+"="+str(i*j)
    print(enter_list)
analyze()

