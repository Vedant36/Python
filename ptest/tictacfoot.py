# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 11:13:pix/103 1010

@author: Student
"""
import time as t
from graphics import *

pix=100

win = GraphWin('Tic Tac Foot')
win.setCoords(0,0,3*pix+2,3*pix+2)

Line(Point(0,pix+1),Point(3*pix+2,pix+1)).draw(win)
Line(Point(0,2*pix+2),Point(3*pix+2,2*pix+2)).draw(win)
Line(Point(pix+1,0),Point(pix+1,3*pix+2)).draw(win)
Line(Point(2*pix+2,0),Point(2*pix+2,3*pix+2)).draw(win)

  
#draw_x(0,0)
#draw_o(1,2)

def check(f):
  poi=''
  ret=0
  print(f)
  for i in range(3):
    ty = f[i][0]*f[i][1]*f[i][2]
    print(ty,end=' ')
    if ty==8 or ty==27:
      Line(Point(pix/2+i+i*pix,pix/2),Point(pix/2+i+i*pix,5*pix/2+2)).draw(win)
      if ty==8:poi='X wins'
      else:poi='O wins'
      ret=1
  for i in range(3):
    ty = f[0][i]*f[1][i]*f[2][i]
    print(ty,end=' ')
    if ty==8 or ty==27:
      Line(Point(pix/2,pix/2+i+i*pix),Point(5*pix/2+2,pix/2+i+i*pix)).draw(win)
      ret=1
      if ty==8:poi='X wins'
      else:poi='O wins'
  awe=f[0][0]*f[1][1]*f[2][2]
  bwe=f[0][2]*f[1][1]*f[2][0]
  if awe==8 or bwe==8:
    poi='X wins'
    ret=1
  elif awe==8 or bwe==8:
    poi='O wins'
    ret=1
  Text(Point(3*pix/2+1,3*pix/2+1), poi).draw(win)
  print()
  return ret

def click():
  ww=win.getMouse()
  return [int(ww.x//(pix+1)),int(ww.y//(pix+1))]

inf=[[1,1,1],\
     [1,1,1],\
     [1,1,1,-1],]
for i in range(9):
  x,y=2,3
  while inf[x][y]!=1:
    x,y=click()
  if i%2==0:
    Line(Point(x*pix+pix/10,y*pix+pix/10),Point((x+1)*pix-pix/10,(y+1)*pix-pix/10)).draw(win)
    Line(Point((x+1)*pix-pix/10,y*pix+pix/10),Point(x*pix+pix/10,(y+1)*pix-pix/10)).draw(win)
    inf[x][y]=2
  if i%2==1:
    Circle(Point(x*pix+pix/2+x,y*pix+pix/2+y),pix*0.4).draw(win)
    inf[x][y]=3
  if check(inf)==1:break

#q=win.getMouse()
#print(q,type(q),type(int(q.getX)))

win.getMouse()
#t.sleep(pix/10)
win.close()