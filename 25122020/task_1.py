def my_func_div(a, b):
    if a != 0 and b != 0:
        return a // b
    else:
        return 'Деление на ноль!'


x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
print(my_func_div(x, y))
