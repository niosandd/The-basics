from random import randint, choice


class House:
    food = 50
    money = 0


class Person:

    def __init__(self, name):
        self.name = name
        self.satiety = 50

    def eat(self):  # ест
        self.satiety += 1
        House.food -= 1
        return f'ест, сытость {self.satiety} еда {House.food}'

    def work(self):  # работает
        self.satiety -= 1
        House.money += 1
        return f'работает, сытость {self.satiety} деньги {House.money}'

    def repast(self):  # идет в магазин
        House.food += 1
        House.money -= 1
        return f'идет в магазин, еда {House.food} деньги {House.money}'

    def play(person):
        number_cubes = randint(1, 6)
        if person.satiety < 0:  # голоден - умер. завершаем эксперимент
            print(f'К сожалению, {person.name} помер с голоду ')
            return 1
        if person.satiety < 20 and House.food >= 10:
            text = person.eat()
        elif House.food < 10:
            text = person.repast()
        elif House.money < 50:
            text = person.work()
        elif number_cubes == 1:
            text = person.work()
        elif number_cubes == 2:
            text = person.eat()
        else:
            text = person.play()
        print(person.name, text)
        return 0

person_1 = Person('Вася')
person_2 = Person('Федя')

for i in range(365):  # пробуем прожить год
    if Person.play(person_1) or Person.play(person_2):
        print('все плохо')
if i == 364:
    print('выжили')


