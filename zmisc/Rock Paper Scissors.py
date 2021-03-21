import math as m
import random as r
w=l=0
print('                   Welcome to the Dangerousest game ever!')
print('                          Rock Paper Scissors!')
print("Rock        1\nPaper       2\nScissors    3\nEnd Game    4\nTrash       Any other number")
while 1!=2:
    mac=r.randint(1,3)
    user=int(input("Enter your choice:"))
    if user==4:
        print("Wins:",w,"Lost:",l)
        break
    elif user>4:
        l+=1
        print("I won 'cause you don't know counting!")
    elif 0<user<4:
        if mac==(user+1)%3:
            print("I won!")
            l+=1
        if mac==(user-1)%3:
            print("You won!")
            w+=1
        if mac==(user)%3:
            print("Guess that's a draw then!")
    else:
        print("Negative numbers kill!")
        l+=1
    print(mac)
