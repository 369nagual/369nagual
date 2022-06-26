# -*- coding: utf-8 -*-
from random import randint


def factorial_v1(n):
    num = 1
    while n >= 1:
        num *= n
        n -= 1
    return num


def factorial_v2(n):
    if n == 1:
        return 1
    return n * factorial_v2(n - 1)


def find(html, element="jobs"):
    if element in html:
        return html[element]
    for key, sub_html in html.items():
        result = find(sub_html, element)
        if result:
            break
    else:
        result = None
    return result


class Backpack:
    def __init__(self):
        self.contents = []

    def add_content(self, item):
        if isinstance(item, list) or isinstance(item, tuple) or isinstance(item, set):
            for el in item:
                self.contents.append(el)
            items = ", ".join(item)
            print(f'{items} added to Backpack')
        else:
            self.contents.append(item)
            print(f'{item} added to Backpack')

    def inspect(self):
        if self.contents:
            print(f'В рюкраке лежит:')
            for i, element in enumerate(self.contents):
                print(f'{i} - {element}')
        else:
            print('There is nothing in your Backpack')


html_dom = {
    "head": {
        "title": {
            "text": {
                "somewhere": {

                }
            }
        },
        "exit": {
            "1": {
                "1.1": {
                    "jobs": "title"
                }
            }
        }
    }
}


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.food = 10
        self.money = 0

    def __str__(self):
        return "Я - {} мой голод  {}, еда {} и денег {}!".format(self.name, self.fullness, self.food, self.money)

    def eat(self):
        print("eating")
        if self.food >= 10:
            self.food -= 10
            self.fullness += 10
        else:
            print("Еда кончилась!")

    def work(self):
        print("working")
        self.money += 50
        self.fullness -= 10

    def play(self):
        print("playing")
        self.fullness -= 10

    def shopping(self):
        print("shopping")
        self.money -= 50
        self.food += 50

    def act_randomly(self):
        if self.fullness <= 0:
            print("{} умер!".format(self.name))
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.food < 10:
            self.shopping()
        elif self.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play()


# from pyatspi import role


class Road:
    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance


class WareHouse:
    def __init__(self, name, content=0):
        self.name = name
        self.content = content
        self.road_out = None
        self.queue_in = []
        self.queue_out = []

    def __str__(self):
        return f"Склад {self.name} груза {self.content} "

    def set_road_out(self, road):
        self.road_out = road

    def truck_arrival(self, truck):
        self.queue_in.append(truck)
        print(f"{self.name} Прибыл грузовик  {truck}")

    def get_next_track(self):
        pass

    def track_ready(self, truck):
        self.queue_out.append(truck)
        print(f"{self.name} грузовик готов {truck}")

    def act(self):
        while self.queue_out:
            truck = self.queue_out.pop()
            truck.go_to(road=self.road_out)


class Vehicle:
    fuel_rate = 0

    def __init__(self, model):
        self.model = model
        self.fuel = 0

    def __str__(self):
        return f"Модель {self.model} имеет {self.fuel} бензина"

    def tank_up(self):
        self.fuel += 1000
        print(f"")


class Truck(Vehicle):
    def __init__(self, model, body_space=1000):
        super().__init__(model=model)
        self.body_space = body_space
        self.cargo = 0
        self.velocity = 100
        self.place = None
        self.distance_to_target = 0

    def __str__(self):
        res = super().__str__()
        return res + f"груза {self.cargo}"

    def ride(self):
        if self.distance_to_target > self.velocity:
            self.distance_to_target -= self.velocity
        print(f"{self.model} едет по дороге, осталось {self.distance_to_target}")

    def go_to(self, road):
        self.place = road
        self.distance_to_target = road.distance
        print(f"{self.model} выехал в путь")

    def act(self):
        if self.fuel <= 10:
            self.tank_up()
        elif isinstance(self.place, Road):
            self.ride()


class Autoloader(Vehicle):
    def __init__(self, model, bucket_capacity=100, warehouse=None, role="loader"):
        super().__init__(model=model)
        self.bucket_capacity = bucket_capacity
        self.warehouse = warehouse
        self.role = role
        self.truck = None

    def __str__(self):
        res = super().__str__()
        return res + f" грузим {self.truck}"

    def act(self):
        if self.fuel <= 10:
            self.tank_up()
        elif self.truck in None:
            self.truck = self.warehouse.get_next_track()
        elif self.role == "loader":
            self.load()
        else:
            self.unload()

    def load(self):
        truck_cargo_rest = self.truck.body_space - self.truck.cargo
        if truck_cargo_rest >= self.bucket_capacity:
            self.warehouse.content -= self.bucket_capacity
            self.truck.cargo += truck_cargo_rest
        else:
            self.warehouse.content -= truck_cargo_rest
            self.truck.cargo += truck_cargo_rest

    def unload(self):
        if self.truck.cargo >= self.bucket_capacity:
            self.truck.cargo -= self.bucket_capacity
            self.warehouse.content += self.bucket_capacity
        else:
            self.truck.cargo -= self.bucket_capacity
            self.warehouse.content += self.bucket_capacity


TOTAL_CARGO = 100000

moscow = WareHouse(name='Moscow', content=TOTAL_CARGO)
piter = WareHouse(name="Piter", content=0)

moscow_piter = Road(start=moscow, end=piter, distance=715)
piter_moscow = Road(start=piter, end=moscow, distance=780)

moscow.set_road_out(moscow_piter)
piter.set_road_out(piter_moscow)

loader_1 = Autoloader(model="Bobcat", bucket_capacity=1000, warehouse=moscow, role="loader")
loader_2 = Autoloader(model="Lonking", bucket_capacity=500, warehouse=piter, role="unloader")

truck_1 = Truck(model="КАМАЗ", body_space=5000)
truck_2 = Truck(model="ГАЗ", body_space=2000)

moscow.truck_arrival(truck_1)
moscow.truck_arrival(truck_2)

hour = 0

while piter.content < TOTAL_CARGO:
    hour += 1
    print(f"=======Час {hour}========")
    truck_1.act()
    truck_2.act()
    loader_1.act()
    loader_2.act()
    moscow.act()
    piter.act()
    print(truck_1)
    print(truck_2)
    print(loader_1)
    print(loader_2)
    print(moscow)
    print(piter)

man = Man(name="Вася")

print(man)
for i in range(1, 366):
    print(f'===day_{i}===')
    man.act_randomly()
    cprint.info(str(man))

print(factorial_v1(9))

print(factorial_v2(9))

print(find(html_dom))

file = open("main.py", "r")

my_back = Backpack()
my_back.inspect()
my_back.add_content("laptop")
my_back.inspect()
my_back.contents.append("so")
my_back.add_content("banana")
my_back.inspect()
my_back.add_content(["tenia", "mozart", "yustas"])
my_back.inspect()

animal = 1
hours = 0
total_exp = [1, 2, 59, 60]


def min_and_sec(variable):
    for e in range(0, 2):
        while total_exp[3 - e] >= min_or_sec:
            variable[3 - e] -= min_or_sec
            variable[2 - e] += 1


for i in range(4):
    total_exp.append(int(input("Введите д/ч/м/s")))

# days
if total_exp[0]:
    for k in range(total_exp[0]):
        total_exp[1] += 24

min_or_sec = 60

min_and_sec(total_exp)
for el in range(total_exp[1] // 3):
    hours += 3
    animal *= 2
    print(f"Прошло часов: {hours}")
    print(f"Клеток: {animal}")
    print(f"Часов до конца: {total_exp[1] - hours}")
    print("++++++++++++++++++++++++++++")

# ++++++++++++++++++++++++++
# total_time = int(input("Введите число: "))
cells = 1
total_time = 10
for hour in range(total_time // 3 + 1):
    cells *= 2
    print("Прошло ", hour * 3)
    print("Кол-во клеток", cells)
    print("Осталось часов", total_time - hour * 3)
    print(hour * 3)

# ===========================
# number = int(input("Введите число: "))
number = 9
for n in range(1, number // 2 + number % 2 + 1):
    n = n * 2 - 1
    print(n ** 2)
