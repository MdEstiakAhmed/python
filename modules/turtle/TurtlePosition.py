import turtle
turtle.speed(1)

print(turtle.position())	#see the postion of turtle
turtle.forward(100)
print(turtle.position())
turtle.backward(100)
print(turtle.position())
turtle.right(90)
turtle.forward(100)
print(turtle.position())
turtle.right(90)
turtle.forward(100)
print(turtle.position())

print()

turtle.setposition(325,145)	#set a positon for turtle

turtle.exitonclick()
