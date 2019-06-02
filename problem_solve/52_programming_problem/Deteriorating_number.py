i = 1000
j = 0
k = 1
while i > 0:
    j += 1
    if k % 5 == 0:
        print(i, end='')
    elif k % 5 != 0:
        print(i, '\t', end='')
    k += 1
    if j % 5 == 0 and j != 1000:
        print("\n")
    i -= 1
