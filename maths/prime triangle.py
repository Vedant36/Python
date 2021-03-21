prent=lambda a: print(a,end='')
prent('     ')
for i in range(1,11881):
    c=0
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            c=1
            break
    if c==0:
        prent('█')
    elif c==1:
        prent(' ')
    if (i**0.5)%1==0:
        prent(',\n')
        prent(f'{i:5d}')