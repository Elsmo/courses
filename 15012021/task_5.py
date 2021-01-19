class Stationery:
    title = ''

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return 'Карандашик'


class Pencil(Stationery):
    def draw(self):
        return 'Ручечка'


class Handle(Stationery):
    def draw(self):
        return 'Маркерочек'


a = Handle()
print(a.draw())

b = Pencil()
print(b.draw())

c = Pen()
print(c.draw())