"""
Создайте базовый абстрактный класс “Корень” с методами вычисления корней уравнения и
вывода результатов на экран. Реализуйте производные классы “Линейное уравнение” и “Квадратное уравнение”
с собственными методами вычисления корней и вывода на экран.

* решите самостоятельно, какими свойствами будет обладать каждый из классов, и какие методы необходимо сделать абстрактными.
"""
from math import sqrt
from abc import ABC, abstractmethod


class Root(ABC):
    def __init__(self):
        self.equation = ''
        self.res = []

    @abstractmethod
    def calculate(self):
        pass

    def print(self):
        if len(self.res) == 0:
            print(f'The equation {self.equation!r} has no roots!')
        elif len(self.res) == 1:
            print(f'The root of {self.equation!r} is: {self.res[0]}')
        else:
            print(f'The roots of {self.equation!r} are: {", ".join(map(str, self.res))}')


class Linear(Root):
    # ax + b = 0    ->   x = -b/a
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b
        self.equation = f'{a}x{b:+}=0'

    def calculate(self):
        res = round(-self.b/self.a, 2)
        self.res.append(res)


class Quadratic(Root):
    # ax^2 + bx + c = 0   ->  D = b^2 - 4ac  ->  x = (-b +/- vD) / (2a)
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.equation = f'{a}x^2{b:+}x{c:+}=0'

    def calculate(self):
        D = self.b ** 2 - 4 * self.a * self.c
        if D == 0:
            x = round(-self.b / (2 * self.a), 2)
            self.res.append(x)
        elif D > 0:
            x1 = round((-self.b + sqrt(D)) / (2 * self.a), 2)
            x2 = round((-self.b - sqrt(D)) / (2 * self.a), 2)
            self.res.extend([x1, x2])


l_eq = Linear(3, 7)
l_eq.calculate()
l_eq.print()

print()

q_eq = Quadratic(1, -2, -3)     # roots: 3, -1
q_eq.calculate()
q_eq.print()