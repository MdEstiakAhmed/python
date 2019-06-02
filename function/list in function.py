def LIST(number):
	result=0
	for i in number:
		result+=i
	return result

x=LIST([1,2,3,4,5,6,7,8,9])
print(x)

"""
passing value and list into a function is not same.
passing value: if we pass a value in function and change the value in function, there will be no changed is main variable value.
passing list: if we pass a list in function and change the list in function, there will be changed is main list value.

"""