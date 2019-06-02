def add(n1,n2):
	return n1+n2

def add_multi(n1,n2):
	return n1+n2, n1*n2

num1=int(input("enter a number:"))
num2=int(input("enter a number:"))

x=add(num1,num2)
print(x)

y=add_multi(num1,num2)
print(y)
