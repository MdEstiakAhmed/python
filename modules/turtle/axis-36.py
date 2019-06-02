import turtle
turtle.color("blue")
turtle.speed(0)
count=0
while count<18:
    for i in range(4):
        turtle.forward(150)
        turtle.right(90)
    turtle.right(20)
    count+=1

turtle.exitonclick()
