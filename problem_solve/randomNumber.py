import random

a,b=input("enter the range a to b: ").split()
a=int(a)
b=int(b)

while True:
	y=int(input("guess a number: "))

	x=int((random.randint(a,b)))
	print("random number is:",x)
	print()

	if(x==y):
		print("you win the game")
	else:
		print("you lost the game")

	print()
	x=input("Do yoou want to play? if want then press 'Y' or 'y'. otherwish 'N' or 'n': ")
	if(x=="Y" or x=="y"):
		continue
	else:
		break

	print()
