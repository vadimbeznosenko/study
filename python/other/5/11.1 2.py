"""
Создать класс “Point” для работы с точками на плоскости. Класс должен содержать:
- динамические свойства: координаты точки X и Y;
- статические свойства: количество точек, лежащих на оси X, количество точек, лежащих на оси Y,
количество точек, совпадающих с началом координат;
- классовые методы: увеличить на 1 количество точек, лежащих на оси X, увеличить на 1 количество точек,
лежащих на оси Y, увеличить на 1 количество точек, совпадающих с началом координат;
- статические методы: проверки, лежит ли точка на одной из осей координат или совпадает с началом координат;
- конструктор: вызывает конструктор родительского класса и выводит сообщение о создании новой точки;
- инициализатор: определяет динамические свойства класса и выводит созданный объект на экран;
- деструктор: выводит сообщение о том, что точка удалена;
- методы: перемещение точки по оси X, перемещение точки по оси Y, определение расстояния до начала координат,
вычисление расстояния до заданной точки, сравнение на совпадение и несовпадение с заданной точкой, вывод точки на экран;
* заданная точка - также экземпляр класса “Point”.

Продемонстрировать работу класса и всех его методов.
"""
from math import sqrt


class Point:
    ox_count = 0
    oy_count = 0
    oo_count = 0

    def __new__(cls, *args, **kwargs):
        print('A new point was created.')
        return super().__new__(cls)

    def __init__(self, x, y):
        self.x = x
        self.y = y
        # print('-' * 20)
        self.print_point()
        print('-' * 20)

        Point.add_point(x, y)

    def __del__(self):
        print(f'The point ({self.x}, {self.y}) was deleted.')

    @classmethod
    def inc_ox_count(cls, val=1):
        cls.ox_count += val

    @classmethod
    def inc_oy_count(cls, val=1):
        cls.oy_count += val

    @classmethod
    def inc_oo_count(cls, val=1):
        cls.oo_count += val

    @classmethod
    def add_point(cls, x, y):
        if cls.is_start_point(x, y):
            cls.inc_oo_count()
        elif cls.lies_on_ox(y):
            cls.inc_ox_count()
        elif cls.lies_on_oy(x):
            cls.inc_oy_count()

    @classmethod
    def del_point(cls, x, y):
        if cls.is_start_point(x, y):
            cls.inc_oo_count(val=-1)
        elif cls.lies_on_ox(y):
            cls.inc_ox_count(-1)
        elif cls.lies_on_oy(x):
            cls.inc_oy_count(-1)

    @staticmethod
    def is_start_point(x, y):
        return x == 0 and y == 0

    @staticmethod
    def lies_on_ox(y):
        return y == 0

    @staticmethod
    def lies_on_oy(x):
        return x == 0

    def move_ox(self, x):
        Point.del_point(self.x, self.y)
        self.x += x
        Point.add_point(self.x, self.y)

    def move_oy(self, y):
        Point.del_point(self.x, self.y)
        self.y += y
        Point.add_point(self.x, self.y)

    def dist_to_start_point(self):
        # v((x1 - 0)^2 + (y1 - 0)^2)
        d = sqrt(self.x**2 + self.y**2)
        print(f'The distance to the start point (0,0) is: {d:.2f}')
        return d

    def dist_to_point(self, point):
        # v((x1 - x2)^2 + (y1 - y2)^2)
        x_len = self.x - point.x
        y_len = self.y - point.y
        d = sqrt(x_len**2 + y_len**2)
        print(f'The distance to the point ({point.x}, {point.y}) is: {d:.2f}')
        return d

    def is_the_same_point(self, point):
        res = self.x == point.x and self.y == point.y
        print(f'The point {"coincides" if res else "does not coincide"} with the point ({point.x}, {point.y})')
        return res

    def print_point(self):
        print(f'The point is: ({self.x}, {self.y})')


p = [Point(2, 6), Point(4, 0), Point(0, 3), Point(0, 0), Point(0, 12)]
print(f'Lies on OX: {Point.ox_count}')
print(f'Lies on OY: {Point.oy_count}')
print(f'Coincide with (0, 0): {Point.oo_count}')
print()

p[0].move_ox(5)
p[0].print_point()
p[0].move_oy(5)
p[0].print_point()
print()

p[0].move_ox(-7)    # move to OY:   OY, OX, OY, OO, OY
p[1].move_oy(3)     # move from OX:     OY, -, OY, OO, OY
p[2].move_oy(-3)    # move from OY to OO:   OY, -, OO, OO, OY
p[3].move_ox(9)     # move from OO to OX:   OY, -, OO, OX, OY
print(f'Lies on OX: {Point.ox_count}')
print(f'Lies on OY: {Point.oy_count}')
print(f'Coincide with (0, 0): {Point.oo_count}')
print()

p[0].print_point()
p[0].dist_to_start_point()
p[0].dist_to_point(p[4])
print()

p[0].is_the_same_point(p[0])
p[0].is_the_same_point(p[1])
print()