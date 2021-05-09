import math as m
i=prev=c=error=v1=v2=p=0
e=2.718281828
pi=3.141592653589793
a=input("Enter a expression: ")
v=x=int(input("Enter the approx value of x: "))
p=1
while round(m.fabs(eval(a))+0.4999)!=0:
    x=i
    x+=p
    v1=x
    new1=eval(a)
    x-=2*p
    v2=x
    new2=eval(a)
    if m.fabs(new1)>m.fabs(new2):
        new=x
    else:
        new=x+2*p
        x+=2*p
    v=x
    i+=1
    prev=eval(a)
    vp=x
    c+=1
    print(new1,new2,new,prev,m.fabs(eval(a))+0.4999)
    if new1==0:
        x=v1
        break
    if new2==0:
        x=v2
        break
    if new==0:
        x=v
        break
    if prev==0:
        x=vp
        break
    if c>20:
        error=1
        break
if error==0:
    print("\nThe zero of the given expression is:",x)
else:
    print("overflow")
