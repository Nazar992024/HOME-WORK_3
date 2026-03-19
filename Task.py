import random

class Student:
    def __init__(self, name):
        self.name = name
        self.money = 100
        self.progress = 0
        self.gladness = 50
        self.alive = True

    def to_study(self):
        print(f"--- {self.name} пішов вчитися (Гроші -, Прогрес ++)")
        self.progress += 10
        self.money -= 20
        self.gladness -= 5

    def to_work(self):
        print(f"--- {self.name} пішов працювати (Гроші ++, Прогрес -)")
        self.money += 100  # Нормальна зарплата
        self.progress -= 2
        self.gladness -= 10

    def to_chill(self):
        print(f"--- {self.name} відпочиває (Задоволення ++, Гроші -)")
        self.gladness += 30
        self.money -= 40
        self.progress -= 1

    def live(self, day):
        print(f"День {day}: Гроші={self.money}, Прогрес={self.progress}, Настрій={self.gladness}")


        if self.money < 50:  # 1.
            self.to_work()
        elif self.progress < 20:
            self.to_study()
        elif self.gladness < 20:
            self.to_chill()
        else:
            dice = random.randint(1, 3)
            if dice == 1:
                self.to_study()
            elif dice == 2:
                self.to_work()
            else:
                self.to_chill()

        if self.money < -100:
            print("Гаплик... Банкрут.")
            self.alive = False
        elif self.progress < -20:
            print("Гаплик... Відрахований.")
            self.alive = False

oleg = Student(name="Олег")

for day in range(1, 366):
    if not oleg.alive:
        print(f"Симуляція перервана на {day} дні.")
        break
    oleg.live(day)

if oleg.alive:
    print("\n" + "=" * 30)
    print("УСПІХ! Рік пройдено!")
    print(f"Фінальний рахунок: Гроші = {oleg.money}, Знання = {oleg.progress}")
    print("=" * 30)