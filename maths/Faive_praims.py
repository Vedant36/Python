import time as t
def prchk(n):
  for i in range(2,int(n**0.5)+1): 
    if n%i==0:return 1
  return 0
def find_prime(num,k=1):
  i=int(num+1)
  while True:
    if prchk(i)==0:return i
    i+=k
def con(a,b):return int((str(int(a))+str(int(b))))
def conchek(pr):
  for i in range(len(pr)):
    for j in range(i+1,len(pr)):
      ab=con(pr[i],pr[j])
      ba=con(pr[j],pr[i])
      #print(ab,ba)
      if prchk(ab)+prchk(ba)>0:return 1
  return 0
def prnx(pr,d):
  pr[d]=find_prime(pr[d])
  for i in range(d+1,5):
    if pr[d]==pr[d-1]:pr[d]=find_prime(pr[d])
  return pr
def fapa():
  import time as t
  pr=[3,7,11,13,17]
  for i in range(1,5):
    print(i)
    while True:
      if conchek(pr[0:i+1])==1:pr=prnx(pr,i)
      else: break
      print(pr,i,pr[0:i+1])
      #t.sleep(0.5)
    if conchek(pr)==0:break
    print(pr)
  return pr
a=t.time()
pr=fapa()
print('The required list of numbers is:',pr)
print('Time of Execution:',t.time()-a)
