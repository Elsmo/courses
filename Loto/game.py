from game_functions import check_card, digit_in_card


class CardGenerator:
    pass


class Game:
    @staticmethod
    def play():
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
                    if any([answer == 'Y' and check_card(barrel),
                            answer == 'N' and check_card(barrel) == False]):  # проверка правильности действий игрока
                        if len(barrel) == 1:  # проверка если выпало однозначное число
                            file = file.replace(' ' + barrel + ' ',
                                                ' - ')  # чтобы не заменяло цифры в двухзначных числах, если выпало однозначное число
                        else:
                            file = file.replace(barrel, '-')  # просто заменяем число, если оно двухзначное
                        card.seek(0)  # здесь тоже 'каретку' в начало файла иначе не работает !!!!
                        card.write(file)
                        card.read()
                    else:
                        print('Вы проиграли')
                        break
            if digit_in_card('player.txt') is False:
                print('Вы выиграли')


d = Game
d.play()
