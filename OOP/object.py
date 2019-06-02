import turtle
turtle.speed(1)
t=turtle.Turtle()	#here t is a object of Turtle class of turtle module
T=turtle.Turtle()
s=turtle.Turtle()

t.shape("circle")
T.shape("square")
s.shape("triangle")

t.color("red")
T.color("blue")
s.color("green")

t.speed(1)
T.speed(1)
s.speed(1)

t.left(30)
t.forward(100)
T.right(45)
T.backward(50)
s.left(75)
s.backward(150)
