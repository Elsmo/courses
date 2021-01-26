"""Совместный проект Смоляк Елизаветы и Масалова Владислав;
Игра расчитана на 1го игрока и компьютер;
Если игрок допускает ошибку (не вычеркивает свой бочонок или вычеркивает бочонок, которого у него нет)
игра автоматически заканчивается проигрышем игрока;

Реализация: Отдельные функции мы импортируем из пакета game;
class CardGenerator генерирует рандомные неповторяющиеся числа в карточки
компьютера и игрока;
class Game имеет статический метод play(), в котором используются экземпляры класса CardGenerator;
Он является основным в программе и выводит на печать сгенерированные карточки, а также отображает ходы
и следит за ходом игры"""


from game import *


class CardGenerator:
    def __init__(self, name):
        self.name = name

    def generate_card(self):
        from random import randint
        s = set()
        if self.name == 'User':
            card = '------ Ваша карточка -----\n** **          **    ** ** \n   ** **     **   **    ** \n** **    **    **    ** \n--------------------------'
        else:
            card = '--- Карточка компьютера ---\n      **   ** **     ** ** \n **   ** **       **    ** \n   ** **     **   **    ** \n---------------------------'
        while len(s) < 15:
            number = str(randint(1, 91))
            if number not in s:
                s.add(number)
                if len(number) == 1:
                    card = card.replace('**', ' ' + number, 1)
                else:
                    card = card.replace('**', number, 1)
            else:
                continue
        return card


class Game:
    @staticmethod
    def play():
        user_card = CardGenerator('User').generate_card()
        comp_card = CardGenerator('Computer').generate_card()
        from random import randint
        cnt_barrel = 90
        used_barrels = []
        while digit_in_card(user_card) is True and digit_in_card(comp_card) is True:  # пока в карточке есть числа
            barrel = str(randint(1, 90))
            if barrel not in used_barrels:
                cnt_barrel -= 1
                print(comp_card, end='\n\n')
                print(f'Выпало число {barrel}. Осталось {cnt_barrel} бачонков\n')
                print(user_card, end='\n\n')
                used_barrels.append(barrel)
                answer = input('Вы хотите зачеркнуть число? Y (да)/ N(нет)  ')
                while all([answer != 'Y', answer != 'N']):  # обработка случая с опечаткой игрока
                    answer = input('Вы хотите зачеркнуть число? Y (да)/ N(нет)  ')
                if any([answer == 'Y' and check_card(barrel, user_card),
                        answer == 'N' and check_card(barrel,
                                                     user_card) is False]):  # проверка правильности действий игрока
                    if len(barrel) == 1:  # проверка если выпало однозначное число
                        user_card = user_card.replace(' ' + barrel + ' ',
                                                      ' - ')  # чтобы не заменяло цифры в двухзначных числах
                    else:
                        user_card = user_card.replace(barrel, '- ')  # просто заменяем число, если оно двухзначное
                else:
                    print('Вы проиграли')  # если игрок не заметил бочонок в своей карточке
                    break
                if len(barrel) == 1:  # ход компьютера
                    comp_card = comp_card.replace(' ' + barrel + ' ', ' - ')
                else:
                    comp_card = comp_card.replace(barrel, '- ')
            if all([digit_in_card(user_card) is False, digit_in_card(comp_card) is False]):
                print('Ничья')
            elif digit_in_card(comp_card) is False:
                print('Компьютер победил')
            elif digit_in_card(user_card) is False:
                print('Вы выиграли')


game = Game()
game.play()
