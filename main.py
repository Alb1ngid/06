# ооп
# обьектно ориентированное програмирование
# классы атрибуты магические методы
string = 'qwert'
bool = True
number = 0


# print(type(string))
# print(type(bool))
# print(type(number))


def x2(a):
    q = a * 2
    print(q)


class Car:
    motor = True

    # функция -- метод
    # 1 обычные методы, 2 магические методы
    def __init__(self, name, age, speed):
        self.name = name
        self.age = age
        self.speed = speed

    def __len__(self):
        return len(f'{self.name},{self.age} {self.speed}')

    def __str__(self):
        return f'name is {self.name}\n' \
               f'age is  {self.age}\n' \
               f'speed = {self.speed}\n'

    def x2(self):
        self.age *= 2
        print(self.age)

    def fly(self):
        print(self.name, 'is flying')


car2 = Car('bmw', 2021, 220)
car1 = Car('mersedes', 2020, 222)
# car1.fly()
# car1.name = 'niwa'
# car1.fly()
print(car1.x2())
print(car1)
p = 1
print(p)
# print(type(car2))
# print(type(car1))
# print(car1.speed)
# print(car1.name)
# print(car1.age)
# print(car1)
# print(car2)
# print(len(car1))
