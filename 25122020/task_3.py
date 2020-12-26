def my_func(x, y, z):
    return max(max(x, y), z)


a, b, c = input('Первое число: '), input('Второе число: '), input('Третье число: ')
print('Maximum: ', my_func(a, b, c))
