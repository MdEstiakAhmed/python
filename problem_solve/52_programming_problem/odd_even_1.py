t = int(input())
while True:
    if t != 0:
        if int(input()) % 2 == 0:
            print("even")
        else:
            print("odd")
        t -= 1
    else:
        break
