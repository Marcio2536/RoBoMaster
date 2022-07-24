word=input("Input 4 number and a sign")
sign=word[4]
num_list=[]
length=0
solution=""
result=0
repeat=0
select=""

def decide(x,y):
    z=0
    select=str(x)+str(y)
    z=len(select)
    for i in range(z):
        for j in range(z):
            if i==j:
                continue
            if select[i]==select[j]:
                return True
            else:
                return False

def analyze():
    for i in range(4):
        num_list[i]=word[i]
    for i in range(4):
        now=num_list[i]
        pre=num_list[i-1]
        if pre==now:
            repeat=now
    for i in range(4):
        for j in range(4):
            num_list.append(str(num_list[i])+str(num_list[j]))
    length=len(num_list)
    for i in range(length):
        num_list[i]=int(num_list[i])
    num_list.sort(reverse=True)
    length=len(num_list)
    if sign=="+":
        plus()
    elif sign=="-":
        minus()
    elif sign=="*":
        multi()
    else:
        divid()

def plus():
    plist=[]
    for i in range(length):
        if num_list[i]>24:
            plist[i]=num_list[i]
    length=len(plist)
    for i in range(length):
        for j in range(length):
            if (decide(plist[i],plist[j]))==True:
                continue
            result=plist[i]+plist[j]
            if result==24:
                solution=str(i)+"+"+str(j)+"="+str(i*j)
    print(solution)

def minus():
    mlist0=[]
    mlist1=[]
    length0=len(mlist0)
    length1=0
    for i in range(length):
        if i>24:
            mlist0[i]=num_list[i]
        elif i<24:
            mlist1[i]=num_list[i]
        else:
            mlist0[i]=mlist1[i]=num_list[i]
    mlist0.sort(reverse=True)
    length0=len(mlist0)
    length1=len(mlist1)
    for i in range(length0):
        for j in range(length1):
            if (decide(mlist0[i],mlist1[j]))==True:
                continue
            result=mlist0[i]-mlist1[j]
            if result==24:
                solution=str(mlist0[i])+"-"+str(mlist1[j])+"="+str(mlist0[i]*mlist1[j])

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
