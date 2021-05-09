import random as r

# q='''`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'''
q='qwertyuiopasdfghjklzxcvbnm   yeeeet'

for i in range(1):
    w=''
    for j in range(16030):
        w += str(r.choice(q))
    print(str(w),end='  ')
# lol=list('1234567890')
# r.shuffle(lol)
# print(lol)