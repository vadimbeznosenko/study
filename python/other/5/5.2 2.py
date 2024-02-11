"""
Изменить класс “Вектор” следующим образом:
- добавить конструктор с выводом сообщения о том, что объект создан;
- добавить  инициализатор, в котором будут задаваться исходные значения объекта;
- добавить деструктор с выводом сообщения о том, что объект удален.

-------------
Тестовые значения:
(4, 12, 6) -> 14
(3, 7, 2) -> 7.87
"""
from math import sqrt


class Vector():
    start_point = (0, 0, 0)

    def __new__(cls, *args, **kwargs):
        print('--This is contructor--')
        return super().__new__(cls)

    def __init__(self, x, y, z):
        print('--This is initializator--')
        self.end_point = (x, y, z)
        # вычисляем координаты вектора, исходя из координат точек начала и конца
        self.x = x - Vector.start_point[0]
        self.y = y - Vector.start_point[1]
        self.z = z - Vector.start_point[2]

    def __del__(self):
        print('--This is destructor--')

    @classmethod
    def set_start_point(cls, x, y, z):
        cls.start_point = (x, y, z)

    def print(self):
        print(f'Vector({self.x}; {self.y}; {self.z})')

    @staticmethod
    def calc_length(x, y, z):
        return sqrt(x**2 + y**2 + z**2)

    def get_length(self):
        # len(v) = v(x^2 + y^2 + z^2)
        length = Vector.calc_length(self.x, self.y, self.z)
        return round(length, 2)

    def multiply(self, num):
        self.x *= num
        self.y *= num
        self.z *= num
        print('New vector: ')
        self.print()


Vector.set_start_point(1, 1, 5)

v1 = Vector(4, 12, 6)
v1.print()
print(f'Module: {v1.get_length()}')
v1.multiply(5)
v1.multiply(3)

print()
v2 = Vector(3, 7, 2)
v2.print()
print(f'Module: {v2.get_length()}')
v2.multiply(5)
v2.multiply(3)