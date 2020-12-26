month = int(input('Введите месяц числом от 1 до 12: '))
seasons = [(1, 2, 12, 'Winter'), (3, 4, 5, 'Spring'), (6, 7, 8, 'Summer'), (9, 10, 11, 'Autumn')]
for i in seasons:
    for j in i:
        if month == j:
            print(i[-1])