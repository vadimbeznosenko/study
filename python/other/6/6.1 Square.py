from math import sqrt


class Square:
    def __init__(self, side):
        self.side = side

    def calc_diagonal(self, to_print=True):
        d = round(self.side * sqrt(2), 2)
        if to_print:
            print(f'Diagonal: {d}')
        return d

    def calc_perimeter(self):
        p = 4 * self.side
        print(f'Perimeter: {p}')
        return p

    def calc_square(self, to_print=True):
        s = self.side ** 2
        if to_print:
            print(f'Square: {s}')
        return s

    def get_info(self):
        return f'Square: side = {self.side}'