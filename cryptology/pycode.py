'''
Ceaser shift ( x+c)%26,   c->I, c->[0,26)
Affine Shift (ax+b)%26, a,b->I, 
Substitution Cipher
Vignere
Transposition
Atbash

lorentz cipher
enigma cipher

ceaser brute force print
Frequency Analysis - word and letter
index of coincidence 0.0686 - 0.038466
double transposition repeating pattern

mutltilingual support
'''

alp='abcdefghijklmnopqrstuvwxyz'

def key_from_word(asd):
  return ''.join([asd[i] for i in range(len(asd)) if asd.index(asd[i])==i])

def pure(code,alp):
  if len(alp)==1:return alp*let(code).count(alp)
  return ''.join([i for i in code if i in alp])

def ioc(code,alp=alp):
  qua=lambda a: len(a)*(len(a)-1)
  return sum([qua(pure(code,i)) for i in alp])/qua(let(code))

def con(code,key):
  sol=[]
  for j in code:
    if j in alp: sol.append(alp[key.index(j)])
    elif j=='-':sol.append('-')
    else:sol.append(j)
  return ''.join(sol)

def let(code,alp=alp):
  return ''.join([i for i in code if i in alp])

class Code:
  def __init__(self,code,conserve_case=False):
    self.code = code.lower()
    if not conserve_case:
      self.case = None
    else:
      self.case = [int(i==i.lower) for i in code]
    self.all=dict(enumerate(['ceaser','affine','map','substitution','transposition','vignere','random']))
    self.alp='abcdefghijklmnopqrstuvwxyz'
    self.let=''.join([i for i in self.code if i in self.alp])#let(code,alp=self.alp)

  def cipher(self,kind=None,key=None):
    if kind is None:
      return self.code
    if type(kind)==int:kind=self.all[kind]
    elif kind=='ceaser':
      if type(key)==str:
        key=ord(key)-97
    self.key=''.join([self.alp[(i+key)%26] for i in range(26)])
    print(self.key)
    return ''.join(self.con(self.code,self.key))

  def decipher(self,kind=None,key=None):
    if kind is None:
      return self.code

    elif kind=='ceaser':
      pass

  def solve(self,kind=None):
    pass
