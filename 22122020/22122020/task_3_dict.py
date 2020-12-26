month = input('Введите месяц числом от 1 до 12: ')
seasons = {'Winter': ['1', '2', '12'], 'Spring': ['3', '4', '5'], 'Summer': ['6', '7', '8']
    , 'Autumn': ['9', '10', '11']}
for key in seasons:
    if month in seasons[key]:
        print(key)