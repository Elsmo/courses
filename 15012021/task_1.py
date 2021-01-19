import time
from itertools import cycle


class TrafficLight:
    def __init__(self, color=''):
        self.__color = color

    def running(self):
        self.__color = cycle(['red', 'yellow', 'green'])
        timer = cycle([7, 2, 5])
        while True:
            print(next(self.__color))
            time.sleep(next(timer))


a = TrafficLight()
a.running()
