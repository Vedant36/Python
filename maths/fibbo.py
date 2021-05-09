n=15#int(input())
f1,f2,i=0,1,0
while i<=n:
    print(f1,end=", ")
    f3=f1+f2
    f1=f2
    f2=f3
    i+=1
print("\b\b")