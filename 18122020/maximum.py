n = int(input('Введите целое положительное число: '))
maximum = n % 10
n = n // 10
while n > 0:
    if n % 10 > maximum:
        maximum = n % 10
        n = n // 10
    else:
        n = n // 10
print(maximum)