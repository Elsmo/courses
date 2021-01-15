with open('ex_5.txt', 'a', encoding='utf-8') as ex_5:
    ex_5.write(input('Вводим циферки через пробел: '))
with open('ex_5.txt', 'r', encoding='utf-8') as new_file:
    print('Сумма всех-всех чисел: ', sum(map(int, new_file.readline().split())))
