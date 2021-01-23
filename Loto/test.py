class CardGenerator:
    pass


# проверка есть ли число в карточке
def check_card(barrel):
    with open('player.txt') as player:
        file = player.read()
        if str(barrel) in file:
            return True
        else:
            return False


# метод который будет проверять остались ли цифры в карточке
def digit_in_card(file_name):
    with open(file_name, 'r', encoding='utf-8') as player_card:
        file = player_card.readlines()
        nums = []
        for lines in file:
            lines = lines.split()
            for elem in range(len(lines)):
                if 1 <= len(lines[elem]) <= 2:
                    nums.append(lines[elem])
        print('Разных чисел в файле ', len(set(nums)), set(nums))
        if len(set(nums)) == 1:
            return False
        else:
            return True



# метод игра#
with open('player.txt', 'r+', encoding='utf-8') as card:
    from random import randint
    cnt_barrel = 90
    used_barrels = []
    while digit_in_card('player.txt') is True:
        card.seek(0)  # 'каретку' в начало файла  иначе не работает !!!!!
        file = card.read()  # читаем содержимое файла
        barrel = str(randint(1, 91))
        if barrel not in used_barrels:
            cnt_barrel -= 1
            print(f'Выпало число {barrel}. Осталось {cnt_barrel} бачонков')
            print(file, end='\n')
            used_barrels.append(barrel)
            answer = input('Вы хотите зачеркнуть число? Y (да)/ N(нет)')
            if any([answer == 'Y' and check_card(barrel), answer == 'N' and check_card(barrel) == False]): # проверка правильности действий игрока
                if len(barrel) == 1:  # проверка если выпало однозначное число
                    file = file.replace(' ' + barrel + ' ', ' - ')  # чтобы не заменяло цифры в двухзначных числах, если выпало однозначное число
                else:
                    file = file.replace(barrel, '-')  # просто заменяем число, если оно двухзначное
                card.seek(0)  # здесь тоже 'каретку' в начало файла иначе не работает !!!!
                card.write(file)
                card.read()
            else:
                print('Вы проиграли')
                break
