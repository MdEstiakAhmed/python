def binary_search(l, x):
	left, right = 0, len(l)-1
	while left <= right:
		mid = (left+right)//2
		if l[mid] == x:
			return mid
		elif l[mid] < x:
			left = mid + 1
		else:
			right = mid - 1
	return "not found"


search_list = [1,5,8,3,6,9,7,44,55,21,59,32,58]
result = binary_search(search_list, 21)
print(result)