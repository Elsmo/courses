words = input('Слова через пробел: ').split()
for i in enumerate(words, 1):
    if len(i[1]) > 10:
        print(i[0], i[1][:10])
    else:
        print(i[0], i[1])