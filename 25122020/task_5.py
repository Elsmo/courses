str_sum = 0


def my_str_sum(num):
    for i in num:
        if i != '#':
            global str_sum
            str_sum += int(i)
        else:
            break
    return str_sum


while True:
    numbers = input('Введите числа через пробел, для выхода в конце укажите "#": ').split()
    print(my_str_sum(numbers))
    if numbers[-1] == '#':
        break
