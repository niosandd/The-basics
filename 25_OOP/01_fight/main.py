import random

class Warrior:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def hit(self, target):
        if type(self) == type(target):
            target.health -= 20
        else:
            raise TypeError

warriors = [Warrior('Воин1'), Warrior('Воин2')]
while True:
    q = input('Введите 1, чтобы какой-то воин атаковал. Для закрытия программы введите 2: ')
    if q == '1':
        i = random.randint(0, 1)
        attacker, victim = warriors[i], warriors[i - 1]
        attacker.hit(victim)
        print(attacker.name, 'атаковал', victim.name)
        print('У', victim.name, 'осталось здоровья', victim.health)
        if victim.health <= 0:
            print(attacker.name, 'победил!!!')
            break
    elif q == '2':
        break
    else:
        print('Ошибка ввода')
