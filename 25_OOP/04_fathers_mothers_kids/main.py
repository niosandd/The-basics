class Parent:
    name = ""
    age = int()
    childList = []

    def __init__(self, name, age, childList):
        self.name = name
        self.age = age
        try:
            self.childList = list(childList)
        except TypeError:
            self.childList.append(childList)

    def info(self):
        print(f"Моё имя {self.name} мне {self.age} лет и у меня {len(self.childList)} детей: ", end="")
        for i in self.childList:
            print(i.name, end=" ")
        print("\n")

    def calmChild(self):
        j = 0
        for i in self.childList:
            print(j, f" = {i.name}")
            j += 1
        childSelect = int(input("Введите номер ребёнка, которого хотите покормить: "))

        if not self.childList[childSelect].calmness:
            self.childList[childSelect].hunger = False
            print(f"Вы успокоили ребёнка с именем {self.childList[childSelect].name}\n")
        else:
            print("Этот ребёнок и так спокоен!\n")

    def feedChild(self):
        j = 0
        for i in self.childList:
            print(j, f" = {i.name}")
            j += 1
        childSelect = int(input("Введите номер ребёнка, которого хотите покормить: "))

        if self.childList[childSelect].hunger:
            self.childList[childSelect].hunger = False
            print(f"Вы покормили ребёнка с именем {self.childList[childSelect].name}!\n")
        else:
            print("Этот ребёнок не голоден!\n")


class Child():
    name = ""
    age = int()
    hunger = True
    calmness = False

    def __init__(self, name, age, hunger, calmness):
        self.name = name
        self.age = age
        self.hunger = hunger
        self.calmness = calmness


def createParent(name, age, childs):
    parent = Parent(name, age, childs)
    return parent


def createChild(name, age, hunger, calmness):
    child = Child(name, age, hunger, calmness)
    return child


parent1 = Parent("Ольга", 38,
                 (Child("Влад", 16, True, False), Child("Дима", 9, False, True), Child("Лера", 4, True, True)))
parent1.info()
parent1.feedChild()
parent1.calmChild()