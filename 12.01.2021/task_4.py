voc = [('One', 'Один'), ('Two', 'Два'), ('Three', 'Три'), ('Four', 'Четыре')]
with open('ex_4.txt', 'r', encoding='utf-8') as ex_4:
    ex4_new = open('ex4_new.txt', 'a', encoding='utf-8')
    for line in ex_4:
        for eng, rus in voc:
            if eng in line:
                line = line.replace(eng, rus)
                print(line, file=ex4_new)
    ex4_new.close()
print('Проверяем файлик ex4_new.txt, не стесняемся')
