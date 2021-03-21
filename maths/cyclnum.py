import time
aaa=time.time()

n = 4
k = 2

def check(num,n,k):
  #if len(num)!=n**k:ret = False
  #else:
  for i in range(k-1):
    num.append(num[i])
  io = True
  inf = []
  for i in range(n**k):
    rt = ''.join(num[i:i+k])
    io = io and rt not in inf
    if not io : return False
    inf.append(rt)
  if io : return True
  
def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSUVWXYZ"):
  return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

ans=[]
qq=baseN(0,n)
poww=int(n**(n**k-2*k-1)*(n**k-1)/(n-1))+1
print(poww)
bn='0'*n**k
basee=[baseN(i,n) for i in range(poww)]
print('doneee')
for i in range(poww):
  #print(i,ans)
  #inf=[]
  #ert=0  
  bn=basee[i]
  qq='0'*k+'1'+'0'*(n**k-len(bn)-k-1)+bn#'%s1%s%s'%('0'*k,'0'*(n**k-len(bn)-k-1),bn)
  #print(qq,end=' ')
  #if qq in inf:continue
  if check(list(qq),n,k):
    ans.append(qq)
    break
print(ans)
#print(qq)
print(time.time()-aaa)