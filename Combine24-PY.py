from ctypes.wintypes import WORD
import random

word=input("Input 4 number and a sign")
sign=word[4]
num_list=[]
length=0
solution=""

def analyze():
    for i in range(4):
        num_list[i]=word[i]
        for j in range(4):
            num_list.append(str(num_list[i])+str(num_list[j]))
    length=len(num_list)
    for i in range(length):
        num_list[i]=int(num_list[i])
    if sign=="+":
        calculate.plus()
    elif sign=="-":
        pass
        #minus()
    elif sign=="*":
        pass
        #multi()
    else:
        pass
        #divid()
class calculate:
    def plus():
        plist=num_list
        length=len(plist)
        plist.sort(reverse=True)
        for i in range(length):
            if plist[i]>24:
                del plist[i]
        length=len(plist)
        for i in range(plist):
            for j in range(length):
                reslt=plist[i]+plist[j]
                if reslt==24:
                    solution=str(i)+"+"+str(j)+"="+str(i*j)
        print(solution)
    def minus():
        s
analyze()
