"""Вспомогательные функции для проверки
digit_in_card(card_name) используется, чтобы проверить наличие чисел в карточке card_name,
если все числа уже зачеркнуты, то возвращает False;
check_card(barrel, card) проверяет встречается ли выпавшее число barrel в строке card
если такого числа нет, то возвращает False"""


def digit_in_card(card_name):
    nums = []
    card_name = card_name.split()
    for elem in range(len(card_name)):
        if 1 <= len(card_name[elem]) <= 2:
            nums.append(card_name[elem])  # список из чисел и черточек
    if len(set(nums)) == 1:  # множество элементов в файле(если там только черточки, то заканчиваем игру)
        return False
    else:
        return True


def check_card(barrel, card):
    if len(str(barrel)) == 1:  # проверка для однозначных чисел
        if str(' '+barrel+' ') in card:
            return True
        else:
            return False
    if len(str(barrel)) == 2:  # проверка для двухзначных чисел
        if str(barrel) in card:
            return True
        else:
            return False
