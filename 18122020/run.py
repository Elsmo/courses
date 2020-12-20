a = int(input('Пробежал в первый день: '))
b = int(input('Цель: '))
dis = a
day = 1
while dis <= b:
    dis += dis * 0.10
    day += 1
print(day)