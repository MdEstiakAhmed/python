x=(1,2,3)
y='a','hello',1
z=1,

print(x)
print(y)
print(z)
print(x[0])

#######	nested tuple ###########
tpl=(1,2.5,'a','hello',['a','b'],('a','b'))
print(tpl)
print(type(tpl))

print(tpl[0])
print(type(tpl[0]))

print(tpl[1])
print(type(tpl[1]))

print(tpl[2])
print(type(tpl[2]))

print(tpl[3])
print(type(tpl[3]))

print(tpl[4])
print(type(tpl[4]))

print(tpl[4][0])
print(type(tpl[4][0]))

print(tpl[5])
print(type(tpl[5]))

print(tpl[5][0])
print(type(tpl[5][0]))

#create a tuple by taking input is impossible. because tuple in non-mutable.

"""

a=()
n=int(input("enter the number of list="))
for i in range(n):
	num=int(input())
	a.append(num)

print(a)

"""