def myfunc(y=5):
	print("y=",y)

"""
there will be a error. if we make any parameter as a defult argument, 
we must make all the parameter after that defult parameter as a defult parameter.

def defult(x,y=10,z):
	print("x, y, z=",x, y, z)
"""

def defult(x,y=100,z=500):#this will be correct
	print("x, y, z=",x, y, z)

a=10
myfunc(a)
myfunc()

x=20
y=30
z=40
defult(x)
defult(x, y)
defult(x, y, z)