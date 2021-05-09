import math as m
"""n=int(input("Enter a number:"))"""
a=0
r=100
for j in range(r):
    for i in range(j+1):
        a+=(1/(i+1))
    r=a-m.log(j+1)
    print(r)
    a=0
