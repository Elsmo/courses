def fact(n):
    res = 1
    for i in range(1, n):
        res *= i
        yield res


for el in fact(7):
    print(el)