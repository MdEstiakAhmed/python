a,b=1,1
n=5
print("1")
print("1")
for i in range(n-2):
	result=a+b
	a=b
	b=result
	print(result)
