while True:
    n=int(input("input a number="))
    if n<0:
        print("it is negative")
        continue
    if n==0:
        print("it is zero")
        break
    print("square=",n*n)
