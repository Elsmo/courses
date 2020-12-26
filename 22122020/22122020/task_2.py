new_list = (input('Введите через пробел любые данные: ')).split()
if len(new_list) // 2 != 0:
    for i in range(1, len(new_list), 2):
        new_list[i], new_list[i-1] = new_list[i-1], new_list[i]
else:
    for i in range(1, len(new_list) - 1, 2):
        new_list[i], new_list[i-1] = new_list[i-1], new_list[i]
print(new_list)