def linear_search(l, x):
	for i in range(len(l)):
		if l[i] == x:
			return i
	return "not found", i
	# i = 0 
	# while i < len(l):
	# 	if l[i] == x:
	# 		return i
	# 	i += 1
	# if i == len(l):
	# 	return "not found"


search_list = [1,5,8,3,6,9,7,44,55,21,59,32,58]
result = linear_search(search_list, 99)
print(result)