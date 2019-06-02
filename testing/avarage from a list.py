def avarage(LIST):
	l=len(LIST)
	Sum=sum(LIST)
	result=Sum/l
	return result

'''
create a list by using for loop
'''

LIST=[]
for i in range(5):
	num=int(input())
	LIST.append(num)

x=avarage(LIST)
print(x)
