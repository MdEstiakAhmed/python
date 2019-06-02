import math


def divisorgenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

t = int(input())
while True:
    if t != 0:
        n = int(input())
        print(list(divisorgenerator(n)))
        t -= 1
    else:
        break
# print(list(divisorgenerator(100)))
