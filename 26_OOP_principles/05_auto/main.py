import math

class Car:

    def __init__(self, x, y, fi):
        self.x = x

    def move(self, dist):
        self.x = self.x + dist * math.cos(self.fi)

        self.y = self.y + dist * math.sin(self.fi)


class Bus(Car):
    PAY_COEFF = 0.01

    MAX_PASSENGERS = 60

    def __init__(self, x, y, direction):

        super().__init__(x, y, direction)

        self.passengers = 0

        self.money = 0

    def move(self, distance):

        self.money += Bus.PAY_COEFF * self.passengers * distance

        super().move(distance)

    def enter(self, passengers):

        if passengers + self.passengers > Bus.MAX_PASSANGERS:
            print('Достигнута максимальная вместимость автобуса')

            print('Уехать смогли только {:d}'.format(Bus.MAX_PASSANGERS - self.passengers))

            print('Остались {:d}'.format(passengers - (Bus.MAX_PASSANGERS - self.passengers)))

            passengers = Bus.MAX_PASSANGERS - self.passengers

        return passengers

    def exit(self, passengers):

        if passengers > self.passengers:
            print('Вышли все из автобуса')

            passengers = self.passengers

        return passengers

    def __str__(self):

        lines = [

            super().__str__(),

            f'В автобусе {self.passengers} пассажиров',

            f'У водителя {round(self.money, 2)} денег',

        ]

        return '\n'.join(lines)

car = Car(5, 5, 5)
bus = Bus(5, 5, 5)

print(car, bus)