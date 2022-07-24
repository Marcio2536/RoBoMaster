word=input("Input 4 number and a sign")
sign=word[4]
num_list=[]
length=0
solution=""
result=0

def analyze():
    for i in range(4):
        num_list[i]=word[i]
        for j in range(4):
            num_list.append(str(num_list[i])+str(num_list[j]))
    length=len(num_list)
    for i in range(length):
        num_list[i]=int(num_list[i])
    num_list=set(num_list)
    num_list=list(num_list)
    if sign=="+":
        plus()
    elif sign=="-":
        minus()
    elif sign=="*":
        pass
        #multi()
    else:
        pass
        #divid()

def plus():
    plist=num_list
    length=len(plist)
    plist.sort(reverse=True)
    for i in range(length):
        if plist[i]>24:
            del plist[i]
    length=len(plist)
    for i in range(plist):
        for j in range(plist): #lengthalso there will be a repeati number problem, eg: 1789+ will output 17+7=24 which doesn't exist):
            result=plist[i]+plist[j]#I agree; can you try to solve it? I am coding for minusing part
            if result==24:
                solution=str(i)+"+"+str(j)+"="+str(i*j)
    print(solution)

def minus():
    mlist0=num_list
    mlist1=[]
    length0=len(mlist0)
    length1=0
    mlist0.sort(reverse=True)
    for i in range(length0):
        if mlist0[i]<=24:
            mlist1.append(mlist0[i])
            del mlist0[i]
    length0=len(mlist0)
    length1=len(mlist1)
    for i in range(length0):
        for j in range(length1):
            result=mlist0[i]-mlist1[j]
            if result==24:
                solution=str(mlist0[i])+"-"+str(mlist1[j])

def multi():
    mulist=[]
    for i in range(length):
        if num_list[i]<24:
            mulist[i]=num_list[i]
    length=len(mulist)
    for i in range(length):
        for j in range(length):
            result=mulist[i]*mulist[j]
            if result==24:
                solution=str(mulist[i])+"*"+str(mulist[j])+"="+(mulist[i]+mulist[j])

def divid():
    dlist0=[]
    dlist1=[]
    for i in range(length):
        if num_list[i]>24:
            dlist0[i]=num_list[i]
        elif num_list[i]<24:
            dlist1[i]=num_list[i]
        else:
            dlist0[i]=dlist1[i]=num_list[i]
    length0=len(dlist0)
    length1=len(dlist1)
    for i in range(length0):
        for j in range(length1):
            result=dlist0[i]/dlist1[j]
            if result==24:
                solution=str(dlist0[i])+"/"+str(dlist1[j])+"="+(dlist0[i]+dlist1[j])

analyze()
