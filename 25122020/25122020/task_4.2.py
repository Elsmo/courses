def my_func(x, y):
    return ''.join(map(str, ['1 / ', x ** abs(y)]))


a = int(input('Введите положительное число: '))
b = int(input('Введите отрицательное число: '))
print(my_func(a, b))