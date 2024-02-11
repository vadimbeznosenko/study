from math import acos, degrees, sqrt


class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_info(self):
        return f'\u25b3ABC ({self.a}, {self.b}, {self.c})'

    def exists(self):
        if (self.a + self.b > self.c) \
                and (self.a + self.c > self.b) \
                and (self.b + self.c > self.a):
            print(f'{self.get_info()} exists.')
            return True

        print(f'{self.get_info()} does not exist.')
        return False

    def get_sides(self):
        print(f'Sides: {self.a}, {self.b}, {self.c}')
        return self.a, self.b, self.c

    def get_angles(self):
        ac = acos((self.a ** 2 + self.c ** 2 - self.b ** 2) / (2 * self.a * self.c))
        ab = acos((self.a ** 2 + self.b ** 2 - self.c ** 2) / (2 * self.a * self.b))
        cb = acos((self.b ** 2 + self.c ** 2 - self.a ** 2) / (2 * self.b * self.c))

        print(f'\u2220CAB: {ac:.2f} Rad, {degrees(ac):.2f} Grad')
        print(f'\u2220ABC: {ab:.2f} Rad, {degrees(ab):.2f} Grad')
        print(f'\u2220BCA: {cb:.2f} Rad, {degrees(cb):.2f} Grad')

        return ac, ab, cb

    def get_perimeter(self, to_print=True):
        p = self.a + self.b + self.c
        if to_print:
            print(f'Perimeter: {p}')
        return p

    def get_square(self):
        p = self.get_perimeter(to_print=False) / 2
        s = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        print(f'Square: {s:.2f}')
        return s

    def is_equilateral(self):
        is_eq = self.a == self.b == self.c
        print(f'Is equilateral: {is_eq}')
        return is_eq
