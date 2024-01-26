"""
Создать класс “Pair” (пара чисел) со свойствами: числа A и B, - и методами:
изменение чисел, вычисление их произведения и суммы.

Определить производный класс “Right Triangle” (прямоугольный треугольник) со свойствами:
катеты A и B, - и методами:
вычисление гипотенузы и площади треугольника, вывод информации о фигуре на экран.

Продемонстрировать работу класса-наследника и всех его методов.
"""
from math import sqrt


class Pair:
    def __init__(self, a, b):
        self.A = a
        self.B = b

    def edit_a(self, a):
        self.A = a

    def edit_b(self, b):
        self.B = b

    def sum(self):
        return self.A + self.B

    def mult(self):
        return self.A * self.B


class RightTriangle(Pair):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.C = self.hypot()

    def hypot(self):
        hypot = round(sqrt(self.A **2 + self.B**2), 2)
        print(f'The hypotenuse of \u25B3ABC: {hypot}')
        return hypot

    def square(self):
        # S = 1/2 * a * b
        s = round(0.5 * self.mult(), 2)
        print(f'The square of \u25B3ABC: {s}')
        return s

    def print_info(self):
        print(f'The right triangle \u25B3ABC ({self.A}, {self.B}, {self.C})')

    def edit_a(self, a):
        super().edit_a(a)
        self.C = self.hypot()

    def edit_b(self, b):
        super().edit_b(b)
        self.C = self.hypot()


tr = RightTriangle(5, 8)
tr.print_info()
tr.square()

print()

print(f'SUM: {tr.sum()}')
print(f'MULT: {tr.mult()}')

print()

tr.edit_a(10)
tr.edit_b(20)
print(f'SUM: {tr.sum()}')
print(f'MULT: {tr.mult()}')
tr.square()