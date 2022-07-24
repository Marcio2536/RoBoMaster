from ctypes.wintypes import WORD
import random

word=input("Input 4 number and a sign")
sign=word[4]
num_list=[]
length=0

def analyze():
    for i in range(4):
        num_list[i]=word[i]
        for j in range(4):
            num_list.append(str(word_list[i])+str(word_list[j]))
    length=len(num_list)
    for i in range(length):
        num_list[i]=int(num_list[i])
    if sign=="+":
        plus()
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
        plist=word_list
        length=len(plist)
        plist.sort(reverse=True)
        for i in range(length):
            if plist[i]>24:
                del plist[i]
            for j in range(length):
                reslt=plist[i]+plist[j]
                if reslt==24:
                    solution=str(i)+"+"+str(j)+"="+str(i*j)
        print(word_list)
analyze()
