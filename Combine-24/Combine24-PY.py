word=input("Input 4 number and a sign")
sign=word[4]
num_list=[]
length=0
solution=""
result=0
repeat=0
select=""

def plus():
    plist=[]
    for i in range(length):
        if num_list[i]<24:
            plist.append(num_list[i])
    print(plist)
    plength=len(plist)
    for i in range(plength):
        for j in range(plength):
            if (decide(plist[i],plist[j])==True) or (i==j):
                continue
            result=plist[i]+plist[j]
            if result==24:
                solution=str(plist[i])+"+"+str(plist[j])+"="+str(plist[i]+plist[j])
                return solution
            for k in range(plength):
                if (decide(plist[i],plist[j],plist[k])==True) or (k==(i or j)):
                    continue                
                result=plist[i]+plist[j]+plist[k]
                if result==24:
                    solution=str(plist[i])+"+"+str(plist[j])+"+"+str(plist[k])+"="+str(plist[i]+plist[j]+plist[k])
                    return solution
                for l in range(plength):
                    if (decide(plist[i],plist[j],plist[k],plist[l])==True) or (l==(i or j or k)):
                        continue
                    result=plist[i]+plist[j]+plist[k]+plist[l]
                    if result==24:
                        solution=str(plist[i])+"+"+str(plist[j])+"+"+str(plist[k])+str(plist[l])+"="+str(plist[i]+plist[j]+plist[k]+plist[l])
                        return solution

def minus():
    global length
    mlist0=[]
    mlist1=[]
    length0=len(mlist0)
    length1=0
    for i in range(length):
        if num_list[i]>24:
            mlist0.append(num_list[i])
        elif num_list[i]<24:
            mlist1.append(num_list[i])
        else:
            mlist0.append(num_list[i])
            mlist1.append(num_list[i])
    print(mlist0)
    print(mlist1)
    length0=len(mlist0)
    length1=len(mlist1)
    for i in range(length0):
        for j in range(length1):
            if (analyze.decide(mlist0[i],mlist1[j]))==True:
                continue
            result=mlist0[i]-mlist1[j]
            if result==24:
                solution=str(mlist0[i])+"-"+str(mlist1[j])+"="+str(mlist0[i]-mlist1[j])
                return solution

def multi():
    global length
    mulist=[]
    for i in range(length):
        if num_list[i]<24:
            mulist.append(num_list[i])
    length=len(mulist)
    for i in range(length):
        for j in range(length):
            if (analyze.decide(mulist[i],mulist[j])==True):
                continue
            print(mulist[i],mulist[j])
            result=mulist[i]*mulist[j]
            if result==24:
                solution=str(mulist[i])+"*"+str(mulist[j])+"="+str(mulist[i]*mulist[j])
                return solution

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
            if (analyze.decide(dlist0[i],dlist1[j])==True):
                continue
            result=dlist0[i]/dlist1[j]
            if result==24:
                solution=str(dlist0[i])+"/"+str(dlist1[j])+"="+(dlist0[i]+dlist1[j])
                return solution

def analyze():
    global length
    for i in range(4):
        num_list.append(int(word[i]))
    for i in range(4):
        for j in range(4):
            if i!=j:
                num_list.append(str(num_list[i])+str(num_list[j]))
                num_list[-1]=int(num_list[-1])
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

def decide(x,y,v=None,w=None):
    z=0
    if v==None and w==None:
        select=str(x)+str(y)
    elif w==None:
        select=str(x)+str(y)+str(w)    
    else:
        select=str(x)+str(y)+str(w)+str(w)
    z=len(select)
    for i in range(z):
        for j in range(z):
            if i==j:
                continue
            if select[i]==select[j]:
                return True
    return False

def main():
    analyze()

main()
