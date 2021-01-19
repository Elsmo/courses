class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def covering(self, mass_asphalt, thickness):
        print(f'Для покрытия дороги понадобится '
              f'{self._length * self._width * mass_asphalt * thickness//1000}т')


r = Road(20, 5000)
r.covering(25, 5)
