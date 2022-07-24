import re
import random
enter=input("Enter 4 number and a sign")
sign=enter[4]
ele=[]
enter_list=[0,0,0,0]
reslt=0
solution=""
length=0
def analyze():
    global length
    for i in range(4):
        enter_list[i]=enter[i]
    for i in range(4):
        for j in range(4):
            enter_list.append(str(enter_list[i])+str(enter_list[j]))
    length = len(enter_list)
    for i in range(length):
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
    length=len(plist)
    plist.sort(reverse=True)
    for i in range(length):
        if plist[i]>24:
            del plist[i]
        for j in range(length):
            reslt=plist[i]+plist[j]
            if reslt==24:
                solution=str(i)+"+"+str(j)+"="+str(i*j)
    print(enter_list)
analyze()
