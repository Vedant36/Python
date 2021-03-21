import matplotlib.pyplot as plt 
import numpy as np
xv=[1,2,3,4] # ist(eval(input('Enter the x values:\n')))
yv=[1, 4, 10, 18] # list(eval(input('Enter the corresponding y values:\n')))
Sx=sum(xv)
Sy=sum(yv)  
Sxy = sum(map(lambda a,b:a*b,xv,yv))
Sx2=sum(map(lambda a:a*a,xv))
n=len(xv)
try:
    c=Sx*Sx-n*Sx2
except:
    c=1
a0=(Sx*Sxy-Sx2*Sy)/c
a1=(Sx*Sy-n*Sxy)/c
qwe=f'a0 = {round(a0,2)}\na1 = {str(round(a1,2))}'
plt.scatter(xv,yv,color= "blue",marker= ".",s=20)
x=np.arange(min(xv)-1,max(xv)+1,0.1)
y=a0+a1*x
plt.plot(x,y,label=qwe)
plt.show()
print(qwe)