import random as rd
import time   as tm

lec=4
cha=12
num=['1','2','3','4','5','6','7','8']
con='y'


print('                    MASTERMIND')
while con[0].lower()!='n':  
  cod=rd.sample(num,4)
  att=tm.time()
  for i in range(cha):
    red=0
    whi=0
    cho=list(input('Enter your combination: '))
    if cho==cod:
      print('You Won! Yeah!')
      print('Time to win: ',tm.time()-att)
      break
    for i in range(lec):
      if cho[i] in cod: whi+=1 
    for i in range(lec):
      if cho[i]==cod[i]: red+=1
    print('R '*red,'W '*(whi-red),'N '*(lec-whi),sep='',end='')
  print(cod)
  
  con=input('Do you want to play again?(y/n): ')
p=input('Press Enter to go bye bye')