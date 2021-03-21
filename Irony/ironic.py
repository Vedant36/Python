'''
TESTING:
open_paren
int 0
add 3
mul 4
close_paren
div 2

FORMATS:
assign :== lhs 
'''
import sys

if len(sys.argv)==1:sys.argv.append("first.ir")

class Module:
  def __init__(self):
    self.built = {
    "out": self.OutputFunc
    }
  def OutputFunc(self, arg):
    print(arg)

class Lexer:
  def __init__(self, code):
    self.encounter_data = False
    self.code = code
  def lex(self, iron):
    tell = 0
    qwe = [[]]
    for i in range(len(iron)):
      if iron[i]=="\"":
        self.encounter_data = not self.encounter_data
      elif iron[i]in{" ", ";", "\n"}:
        if not self.encounter_data:
          qwe[-1].append(iron[tell:i])
          tell = i+1
        if iron[i]=="\n":
          qwe.append([])

    return qwe

  def run(self, qwe):
    for i in qwe:
      for j in i:
        pass
        

with open(sys.argv[1],"r") as file:
  iron = file.read()

module = Module()
lexer = Lexer(module)
qwe = lexer.lex(iron)
print(f"{iron!r}")
from pprint import pprint as pp
pp(qwe)