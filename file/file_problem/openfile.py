capital = 'A'
small = 'a'
i = 0
list1 = []
with open("countrylist.txt", "r") as fp:
    list1 = fp.readlines()
    while i < 26:
        for line in list1:
            x = line[0]
            if x == small or x == capital:
                filename = "new\\" + x + ".txt"
                f = open(filename, "a")
                f.write(line)
                f.close()
        capital = chr(ord(capital) + 1)
        small = chr(ord(small) + 1)
        i += 1




