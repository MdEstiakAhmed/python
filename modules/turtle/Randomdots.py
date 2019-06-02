import turtle
import random

turtle.speed(12)
turtle.pensize(5)
turtle.penup()

color=["red","blue","green","orange","pink","purple","yellow"]

for i in range(100):
	x=random.randint(-200,200)
	y=random.randint(-200,200)
	turtle.setposition(x,y)
	i=random.randint(0,len(color)-1)
	turtle.dot(color[i])

turtle.done()
turtle.exitonclick()
