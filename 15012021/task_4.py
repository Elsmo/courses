class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.is_police:
            print('Полицейская', self.name, 'поехала')
        else:
            print(self.name, 'поехала')

    def stop(self):
        if self.is_police:
            print('Полицейская', self.name, 'остановилась')
        else:
            print(self.name, 'остановилась')

    def turn(self, direction):
        if self.is_police:
            print('Полицейская', self.name, 'повернула', direction)
        else:
            print(self.name, 'повернула', direction)

    def show_speed(self):
        print(self.name, 'speed:', self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости. Ваша {self.speed}. Пожалуйста сбавьте до 60 км/ч')
        else:
            print(self.name, 'speed:', self.speed)


class SportCar(Car):
    def show_speed(self):
        print('Sports car speed: ', self.speed)


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости. Ваша {self.speed}. Пожалуйста сбавьте до 40 км/ч')
        else:
            print(self.name, 'speed:', self.speed)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super(PoliceCar, self).__init__(speed, color, name, is_police)


car_1 = TownCar(65, 'white', 'Lada')
car_2 = WorkCar(50, 'black', 'Kia')
car_3 = SportCar(150, 'red', 'Ferrari')
car_4 = PoliceCar(100, 'blue', 'BMW')

car_1.show_speed()
car_1.stop()
car_2.show_speed()
car_3.show_speed()
car_3.turn('направо')
car_4.go()

