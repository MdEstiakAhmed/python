def selection_sort(l):
   n = len(l)
   for i in range(0, n-1):
   	index_min = i
   	for j in range(i+1, n):
   		if l[j] < l[index_min]:
   			index_min = j
   	if index_min != i:
   		l[i], l[index_min] = l[index_min], l[i]

   return l



sort_list = [5, 6, 10, 3, 4, 52, 22, 2]
result = selection_sort(sort_list)
print(result)