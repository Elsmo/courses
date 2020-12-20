earnings = int(input('Ваша выручка: '))
expenses = int(input('Ваши издержки: '))
if earnings > expenses:
    print('Вы вышли на прибыль в этот раз')
    profit = earnings - expenses
    print('Рентабельность: ', profit / earnings)
    employee = int(input('Сколько у вас работает сотрудников: '))
    print('Прибыль на одного человека: ', profit / employee)
else:
    print('Вы работаете в убыток')