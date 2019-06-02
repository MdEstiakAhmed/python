def selection_sort(l):
    position = 0
    small_element = l[0]
    for i in range (len(l)):
        if l[i] != (len(l) - 1):
            if l[i] > l[i+1]:
                small_element = l[i+1]
                l[i+1] = l[i]
                l[i] = small_element

    return l



sort_list = [5, 6, 10, 3, 4, 52, 22, 2]
result = selection_sort(sort_list)
print(result)