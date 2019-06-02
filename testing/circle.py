import turtle
turtle.speed(15)
turtle.shape("turtle")
turtle.color("maroon")

def star(length):
	for i in range(12):
		turtle.forward(length)
		turtle.left(150)

counter=0
while counter<30:
	star(150)
	turtle.right(12)
	counter+=1

turtle.exitonclick()
