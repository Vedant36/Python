import math
def factor(l):
    e=l
    s=math.sqrt(e)
    i,c=2,0
    print(e," = ")
    while i<s:
        a=int(l%i)
        if a==0:
            if c==0:
                print(i)
            else:
                print("*",i)
            l=l/i
            c+=1
        elif l==1:
            break
        elif l<s:
            break
        else:
            if i==2: i+=1
            elif i==3: i+=2
            elif i%3==1: i+=4
            else: i+=2
    if c==0:
        print("\n",e,"is a prime number.")
    else:
        print("*",int(l))
    # print("\n",l,int(math.sqrt(e)))
    # y=int(len(str(e)))
l=8753195687658375#int(input("Enter a number: "))
factor(l)
