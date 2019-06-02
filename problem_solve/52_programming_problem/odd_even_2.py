t = int(input())
while True:
    if t != 0:
        n = input()
        x = n[-1:]
        if int(x) % 2 == 0:
            print("even")
        else:
            print("odd")
        t -= 1
    else:
        break
