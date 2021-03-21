import math as a
import time as t
def pc(n):  
  if n==1 or n==0:return 0
  for i in range(2,round(n**0.5)+1):
      if n % i == 0:return 0
  return 1
t1=t.time()
a=float(input('Enter no of digits:'))
c,i=0,9999962683#int(10**a-3)
prev=3
while 3<=i<=int(10**a-3):
  for j in range(int(a+1)):
    w=i%(10**j)
    if pc(w)==1:
      c+=1
    #elif pc(w)==0: 
    #print(j)
  if c==a:
    l=i
    print(l)
    if l-prev==4 or l-prev==6:
        qwe=[prev,l]
        break
    prev=l
  #if t.time()-t1>=10:break
  c=0
  i-=int(((10-i%10)+5)/2)
print(l)
print(qwe)
t2=t.time()
print('Execution Time: ',t2-t1)
