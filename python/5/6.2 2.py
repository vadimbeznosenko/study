"""
Изменить созданный ранее класс “Вектор” следующим образом:
- установить для одного из динамических свойств класса модификатор доступа protected,
а для остальных (если имеются) - модификатор доступа private;
- добавить соответствующие методы getter и setter.

"""
from math import sqrt


class Vector():
    start_point = (0, 0, 0)

    def __new__(cls, *args, **kwargs):
        print('--This is contructor--')
        return super().__new__(cls)

    def __init__(self, x, y, z):
        print('--This is initializator--')
        self.set_end_point(x, y, z)
        # вычисляем координаты вектора, исходя из координат точек начала и конца
        self.set_x(x - Vector.start_point[0])
        self.set_y(y - Vector.start_point[1])
        self.set_z(z - Vector.start_point[2])

    def __del__(self):
        print('--This is destructor--')

    def set_end_point(self, x, y, z):
        self._end_point = (x, y, z)

    def get_end_point(self):
        return self._end_point

    def set_x(self, x):
        self.__x = x

    def get_x(self):
        return self.__x

    def set_y(self, y):
        self.__y = y

    def get_y(self):
        return self.__y

    def set_z(self, z):
        self.__z = z

    def get_z(self):
        return self.__z

    @classmethod
    def set_start_point(cls, x, y, z):
        cls.start_point = (x, y, z)

    def print(self):
        print(f'Vector({self.get_x()}; {self.get_y()}; {self.get_z()})')

    @staticmethod
    def calc_length(x, y, z):
        return sqrt(x**2 + y**2 + z**2)

    def get_length(self):
        # len(v) = v(x^2 + y^2 + z^2)
        length = Vector.calc_length(self.get_x(), self.get_y(), self.get_z())
        return round(length, 2)

    def multiply(self, num):
        self.set_x(self.get_x() * num)
        self.set_y(self.get_y() * num)
        self.set_z(self.get_z() * num)
        print('New vector: ')
        self.print()


Vector.set_start_point(0, 0, 0)

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