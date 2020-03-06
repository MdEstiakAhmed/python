import time
start=time.time()
n=int(input("input a number:"))
if (n/2==0):
	print("not prime")
else:
	for i in range(3,n,2):
		if (n/i==0):
			break
	print("not prime")

end=time.time()
print(end-start)