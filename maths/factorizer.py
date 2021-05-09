import math as m
import time as t
import matplotlib.pyplot as plt

# print('Starting...')
def factorize(num):
  if num<4:return [num]
  lim = int(m.sqrt(num))+1
  # print(lim)
  i=2
  # pri=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,83,89,97,101,103]
  fac=[]
  while num!=1:
    # print('1',i,num)
    if num%i==0:
      # print('2',i,num)
      fac.append(i)
      num=num//i
      while num%i==0:
        # print('3',i,num)
        num=num//i
    if i>lim:
      fac.append(num)
      return fac
      
    i+=1
  return fac

# print('Function loaded...')
num = 1987531983751357
# print('Calculating factors...')
print(f'{num} = {factorize(num)}')
# fac=[]
# tim=[]
# for i in range(20):
#   ini=t.time()
#   fac.append(factorize(num))
#   tim[i]=t.time()-ini

# plt.plot(tim,label='factorice')[47, 61, 12576671]
# plt.show