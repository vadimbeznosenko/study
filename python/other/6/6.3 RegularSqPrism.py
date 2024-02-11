from math import sqrt
from Square import Square


class RegualrSqPrism(Square):
    def __init__(self, side, height):
        super().__init__(side)
        self.height = height

    def calc_volume(self):
        v = self.side ** 2 * self.height
        print(f'Volume: {v}')
        return v

    def get_info(self):
        return f'Regular square prisma: base side = {self.side}, height = {self.height}'

    def calc_square(self):
        s = 2 * super().calc_square(to_print=False) + 4 * self.side * self.height
        print(f'Square: {s}')
        return s

    def calc_diagonal(self):
        d = sqrt(self.height ** 2 + super().calc_diagonal(to_print=False))
        print(f'Diagonal: {d}')
        return d