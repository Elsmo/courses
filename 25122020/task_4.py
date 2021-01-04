def my_func(x, y):
    rez = x
    for i in range(1, abs(y)):
        rez = rez * x
    return ''.join(map(str, ['1 / ', rez]))


a = int(input('Введите положительное число: '))
b = int(input('Введите отрицательное число: '))
print(my_func(a, b))