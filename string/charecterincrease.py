listofalphabent = ["A"]
value = 'A'
i = 0
while i < 25:
    listofalphabent.append(chr(ord(value) + 1))
    value = chr(ord(value) + 1)
    i += 1

print(listofalphabent)
