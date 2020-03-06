def showlnlist(n):
    fibolist=[0,1]
    fibofirst,fibonext=fibolist[0],fibolist[1]

    i=3
    while i<=n:
        fibofirst, fibonext = fibonext, fibofirst + fibonext
        fibolist.append(fibonext)
        i+=1
    return fibolist


if __name__=="__main__":
    print(showlnlist(2))
    print(showlnlist(5))
    print(showlnlist(10))
    print(showlnlist(15))
    print(showlnlist(20))
