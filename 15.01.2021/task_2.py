class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def covering(self, _length, _width):
        mass = self._length * self._width
