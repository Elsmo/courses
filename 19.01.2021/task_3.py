from math import ceil


class Cell:
    def __init__(self, cnt):
        self.cnt = cnt

    def __add__(self, other):
        return f'Сумма двух клеток: {self.cnt + other.cnt}'

    def __sub__(self, other):
        if self.cnt - other.cnt >= 0:
            return f'Разность двух клеток: {self.cnt - other.cnt}'
        else:
            return 'Разность клеток не может быть меньше нуля'

    def __mul__(self, other):
        return f'Произведение двух клеток: {self.cnt * other.cnt}'

    def __truediv__(self, other):
        return f'Частное двух клеток: {round(self.cnt / other.cnt, 2)}'

    def make_order(self, row):
        lst_cell = '*' * self.cnt
        for i in range(ceil((self.cnt / row))):
            if len(lst_cell) >= row:
                print(lst_cell[:row])
                lst_cell = lst_cell[row::]
            else:
                print(lst_cell)


a = Cell(10)
b = Cell(12)

a.make_order(6)
print(a + b)
print(a - b)
print(a / b)
print(a * b)
