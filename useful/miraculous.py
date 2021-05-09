import math   as ma
import random as rd
import time   as tm

def nCr(n,r):
  a=1
  for i in range(r):
    a*=(n-i)/(i+1)
  return a

def sumv(ini,fin,eqa,x):
  eqa='x'.join(eqa.split(x))
  asum,var=0,round(ini)
  for i in range(round(ini),round(fin)+1):
    x=i
    asum+=eval(eqa)
    print(x,asum)
  return asum

def det(qwe):
  sam=0
  if len(qwe)==2:return qwe[0][0]*qwe[1][1]-qwe[0][1]*qwe[1][0]
  else:
    for i in range(len(qwe)):
      bat=[]
      for j in range(1,len(qwe)):
        ijr=list(qwe[j])
        ijr.pop(i)
        bat.append(ijr)
      sam+=((-1)**(i+1))*det(bat)*qwe[0][i]
    return sam

def getch():
  from msvcrt import getch
  return getch

class later:
  tag_list={}
  def set(self,var,time=-1):
    self.tag_list[var]=[time,tm.time()if time+1 else 0]
  def up(self):
    for i in self.tag_list:
      pass

class Tok:
  '''Tok.tok is a function to be used as a parameter in
  np.genfromtext as a converter for string as a tokenizer'''
  uni = list()
  @classmethod
  def tok(cls, new):
    if new in cls.uni: return cls.uni.index(new)-1
    cls.uni.append(new)
    return len(cls.uni)-1

class Tok2:
  uni = list()
  def ser(self, num):
    def tok(new):
      if new not in self.uni:self.uni.append(new)
      return [int(new in self.uni[i:i+1]) for i in range(num)]
    return tok

class switch:
  '''men at work: thingy not complete'''
  def __init__(self):
    pass
  def switch(self):
    pass
  def case(self):
    pass

class rep: 
  "avoids returning if new value is the same as the old one" 
  val = None 
  def do(self, *args, **kwargs): 
    if self.val!=args: 
      print(*args, **kwargs) 
      self.val = args 
    else: 
      print(end='') 

class stopwatch():
  def __init__(self):
    self.act = self.now = self.set = None
  def check(self):
    if self.set is None: return 0.
    if self.now is not None: 
      self.act = self.now = round(tm.time() - self.set,5)
    return self.act
  def start(self):
    self.set = tm.time()
    self.now = 0
  def stop(self):
    tm.time()-self.set
    self.now = None
  def reset(self):
    self.act = self.now = self.set = None

def iint(a): 
  return tuple([int(i.real) for i in a]) if hasattr(a, '__iter__') else int(a) 
