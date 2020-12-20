seconds = int(input('Введите время в секундах: '))
minutes = seconds // 60
hours = minutes // 60
print(f'{hours}:{minutes % 60}:{seconds % 60}')