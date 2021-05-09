from math import log10,ceil
# from time import time
# def cha2(num,pwo=2,lim=0):
#   ran=10**lim
#   for i in range(ran):
#     oca=(num*ran+i)
#     # print(oca)
#     if round(oca**(1/pwo))**pwo==oca:
#       return int(oca)
#   return cha2(num,pwo,lim=lim+1)
#
def cha3(num, pwo=2):
  i=0
  while True:
    # print(i**pwo)
    if str(i**pwo).startswith(str(num)):
      return i**pwo
    i+=1

def cha4(num, pwo=2):
  i=0
  while True:
    if i<=300:wo=round(num**(1/pwo)*(10**i)**(1/pwo))
    else:
      wo=num**(1/pwo)
      for j in range(i//300):
        wo*=(10**300)**(1/pwo)
      wo=round(wo*(10**(j%300))**(1/pwo))
      # wo=round(wol)
    # print(i,wo**pwo)
    if str(wo**pwo).startswith(str(num)):
      # print(i)
      return int(wo**pwo)
    i+=1

def cha5(num, pwo=2):
  c=0
  while True:
    wo0=(num**(1/pwo)*(10**c)**(1/pwo))
    wo1=((num+1)**(1/pwo)*(10**c)**(1/pwo))+1
    # print(c,ceil(wo0),int(wo1))
    for i in range(int(wo0),int(wo1)):
      if str(i**pwo).startswith(str(num)):
        return i**pwo
    c+=1

# ma=0
# for i in range(1,6):
#   for j in range(10**(i-1),10**i):
#     che=int(log10(cha5(j,3)))+1
#     if che>ma:
#       ma=che
#   print(f'{i:2} {ma:3}')
for i in range(1,100):
  print(f'{i:>3}', cha5(3605731,i))