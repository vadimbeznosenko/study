"""
Внести изменения в созданные классы следующим образом:
- динамические свойства класса “Point” должны иметь модификатор доступа protected;
- определить методы getter и setter для свойств с модификаторами доступа private и protected;
- любое взаимодействие с private и protected свойствами  должно производиться посредством соответствующих методов getter и setter.

Продемонстрировать работу измененных классов.
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
        self.set_x(x)
        self.set_y(y)
        self.print_point()
        print('-' * 20)

        Point.add_point(x, y)

    def __del__(self):
        print(f'The point ({self.get_x()}, {self.get_y()}) was deleted.')

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y

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
        Point.del_point(self.get_x(), self.get_y())
        self.set_x(self.get_x() + x)
        Point.add_point(self.get_x(), self.get_y())

    def move_oy(self, y):
        Point.del_point(self.get_x(), self.get_y())
        self.set_y(self.get_y() + y)
        Point.add_point(self.get_x(), self.get_y())

    def dist_to_start_point(self):
        # v((x1 - 0)^2 + (y1 - 0)^2)
        d = sqrt(self.get_x()**2 + self.get_y()**2)
        print(f'The distance to the start point (0,0) is: {d:.2f}')
        return d

    def dist_to_point(self, point):
        # v((x1 - x2)^2 + (y1 - y2)^2)
        x_len = self.get_x() - point.get_x()
        y_len = self.get_y() - point.get_y()
        d = sqrt(x_len**2 + y_len**2)
        print(f'The distance to the point ({point.get_x()}, {point.get_y()}) is: {d:.2f}')
        return d

    def is_the_same_point(self, point):
        res = self.get_x() == point.get_x() and self.get_y() == point.get_y()
        print(f'The point {"coincides" if res else "does not coincide"} '
              f'with the point ({point.get_x()}, {point.get_y()})')
        return res

    def print_point(self):
        print(f'The point is: ({self.get_x()}, {self.get_y()})')


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