all_income, worker = 0, 0
min_income = []
with open('ex_3.txt', 'r', encoding='utf-8') as file_new:
    for word in list(file_new):
        all_income += int(word.strip().split()[1])
        worker += 1
        if int(word.strip().split()[1]) < 20000:
            min_income.append(word.strip().split()[0])


print('Оклад меньше 20к: ', *min_income)
print('Средний оклад по всем сотрудикам: ', round((all_income / worker), 2))
