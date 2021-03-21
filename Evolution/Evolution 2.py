import random as r
import time as t
import math as m
e2=0
rngr=1
for qwe in range(rngr):
	rec=1
	e3=0
	for ved in range(0,rec):
		life=1000
		e4=0
		c=0.31
		for i in range(life):
			P=30
			food=F=50
			c=0.31*F/P
			for j in range(P):
				acc=4
				rc=r.randint(1,10**acc)/10**acc
				if rc<c/(1-c):
					oxa=m.floor(m.log(c-rc*(1-c))/m.log(c))
					if F>=oxa:
						F-=oxa
						P+=oxa-1
					else:
						P-=1
				else:
					oxa=0
					P-=1
				#print(P,oxa)
				#print(P)
			if P==0:break
			e4+=P
			F=food
			print(P,'-',c,end=' ')
		#print(ved,'Population:',P)	
		#t.sleep(2)
		#print('This Species lived:',i,'days')
		print('Average Population=',e4/i)
		e3+=e4/life
	#print(round(e3/(rec),2))
	e2+=e3/(rec)
print(e2/rngr)
