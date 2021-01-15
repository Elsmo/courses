all_lessons = {}
letters_replace = ['(л)', '(пр)', '(лаб)', '—']

with open('ex_6.txt', 'r', encoding='utf-8') as data_file:
    for line in data_file:
        for i in letters_replace:
            if i in line:
                line = line.replace(i, '')
        all_lessons.update({line.split()[0]: sum(map(int, line.split()[1:]))})
print(all_lessons)