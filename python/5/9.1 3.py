"""
Создайте базовый абстрактный класс “Функция” с методами вычисления значения функции
y=f(x) в заданной точке x и вывода результата на экран.

Реализуйте производные классы
“Эллипс” (x^2/a^2+y^2/b^2=1) и “Гипербола” (x^2/a^2-y^2/b^2=1) с собственными методами
вычисления значения функции в заданной точке.

* решите самостоятельно, какими свойствами будет обладать каждый из классов,
и какие методы необходимо сделать абстрактными.
"""
from math import sqrt
from abc import ABC, abstractmethod


class Function(ABC):
    def __init__(self):
        self.func = ''
        self.points = {}        # {1: [2, 3, 4], 2: [], 3: [4]}

    @abstractmethod
    def calculate(self, x):
        pass

    def print(self, x=None):
        if x is None:
            points_str = []
            for key, val in self.points.items():
                for v in val:
                    points_str.append(f'({key}, {v})')
            points_str = ', '.join(points_str)
            print(f'The {self.func!r} has points: {points_str}')

        elif x not in self.points.keys():
            print(f'No data for x={x}')
        elif len(self.points[x]) == 0:
            print(f'The {self.func!r} has not point for x={x}')
        else:
            points_str = map(lambda y: f'({x}, {y})', self.points[x])
            points_str = ', '.join(points_str)
            print(f'The {self.func!r} has points: {points_str}')


class Ellipse(Function):
    # x^2/a^2+y^2/b^2=1     ! a>=b>0
    # y^2/b^2 = 1 - x^2/a^2
    # y^2 = b^2(1 - x^2/a^2)
    # y = +/- bv(1-x^2/a^2)

    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b
        self.func = f'x^2/{a}^2 + y^2/{b}^2 = 1'

    def calculate(self, x):
        if x in self.points.keys():
            return

        tmp = 1 - x ** 2 / self.a ** 2
        if tmp == 0:
            self.points[x] = [0]
        elif tmp > 0:
            y1 = round(self.b * sqrt(tmp), 2)
            y2 = - y1
            self.points[x] = [y1, y2]
        else:
            self.points[x] = []


class Hyperbola(Function):
    # x ^ 2 / a ^ 2 - y ^ 2 / b ^ 2 = 1     ! a,b>0
    # - y^2/b^2 = 1 - x^2/a^2
    # - y^2 = b^2(1 - x^2/a^2)
    # y = +/- bv(x^2/a^2 - 1)

    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b
        self.func = f'x^2/{a}^2 - y^2/{b}^2 = 1'

    def calculate(self, x):
        if x in self.points.keys():
            return

        tmp = x ** 2 / self.a ** 2 - 1
        if tmp == 0:
            self.points[x] = [0]
        elif tmp > 0:
            y1 = round(self.b * sqrt(tmp), 2)
            y2 = - y1
            self.points[x] = [y1, y2]
        else:
            self.points[x] = []


e = Ellipse(5, 3)
e.calculate(x=5)    # y = 0
e.calculate(x=0)    # y = 3, -3
e.calculate(x=2)    # y = 2.75, -2.75
e.calculate(x=10)

e.print(x=5)
e.print(x=0)
e.print(x=2)
e.print(x=8)
e.print(x=10)
e.print()

print('*'*50)

h = Hyperbola(3, 4)
h.calculate(x=-3)   # Y = 0
h.calculate(x=5)    # y = 5.33, -5.33
h.calculate(x=7)    # y = 8.43, -8.43
h.calculate(x=0)

h.print(x=-3)
h.print(x=5)
h.print(x=7)
h.print(x=8)
h.print(x=0)
h.print()