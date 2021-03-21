import random
p=print
w=f=0
c="y"
l=0
p("					  Welcome to the number guessing game")
p("					 I am thinking of a number from 1 to 6")
p("								 GUESS IT")   
while c[0]!="n":
	a=random.randint(1,6)
	for i in range(3):
		b=int(input("Enter you guess: "))
		if b==a:
			p("Your answer is correct")
			w+=1
			break
		else:
			if i==2:
				l+=1
			else:
				p("WRONG!WRONG!WRONG!",3-i-1,"chances left",sep=" ")
				i+=1
		f+=1
	if f==3:
		p("The number was:",a)
	c=input("\nDo you want to play this game again?")
p("\n\nThanks for playing")
p("Wins=",w,"\nLost=",l)
q=input("press any key to continue!")
