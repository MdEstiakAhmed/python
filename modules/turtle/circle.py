import turtle
turtle.speed(15)

def draw_square(length):
	for i in range(4):
		turtle.forward(length)
		turtle.left(90)

counter=0
while counter<90:
	draw_square(100)
	turtle.right(4)
	counter+=1

turtle.exitonclick()
