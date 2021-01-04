from functools import reduce


res = 1
# even_numbers = list([x for x in range(100, 1001) if x % 2 == 0])
even_numbers = list([x for x in range(1, 10) if x % 2 == 0])
result = reduce(lambda res, i: res * i, even_numbers)
print(result)
