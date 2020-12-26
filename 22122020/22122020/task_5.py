rating_list = [5, 3, 2, 1]
new_ball = 1
while new_ball != 0:
    new_ball = int(input('Введите новый элемент рейтинга: '))
    rating_list.append(new_ball)
    print(*sorted(rating_list)[::-1])