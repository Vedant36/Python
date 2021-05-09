import random as r
import time as t
e2=0
for qwe in range(100):
    rec=37
    e3=0
    for ved in range(1,rec):
        nc=1000
        life=50
        avg=0
        d1=0.4
        food=10
        q=1
        for i in range(life):
            for j in range(1):
                r.seed(i)
                e4=round(16*food/nc)
                p=r.randint(0,e4)
                if p in range(0,round(d1*e4)):
                    a=0
                    nc-=1
                elif p in range(round(d1*e4),round(d1*d1*e4)):
                    a=1
                else:
                    a=2
                    nc+=1
                if nc==0:break
            # print('Population:',nc)
            avg+=nc
            if nc<=0:
                q=i
                break
        print(ved,end=' ')
        print('This Species lived:',i,'days')
        print('Average Population:',avg/q)
        e3+=avg/q
    print(round(e3/(rec-1),2))
    e2+=e3/(rec-1)
print(e2/100)
