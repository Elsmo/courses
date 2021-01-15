lines, word = 0, 0
words = {}
with open('ex_2.txt', 'r', encoding='utf-8') as file_new:
    for line in file_new:
        word = len(line.split())
        lines += 1
        words.update({lines: word})
        word = 0
print('Всего строк в файлике: ', lines)
for i in words.keys():
    print(f'В строке {i} всего {words.get(i)} слов')
