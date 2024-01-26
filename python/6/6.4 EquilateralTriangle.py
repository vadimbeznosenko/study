from math import degrees, pi
from Triangle import Triangle


class EquilateralTriangle(Triangle):
    def __init__(self, a):
        super().__init__(a, a, a)

    def is_equilateral(self):
        print('Is is equilateral.')
        return True

    def get_angles(self):
        angle = pi/3
        print(f'\u2220CAB == \u2220ABC == \u2220BCA: {angle:.2f} Rad, {degrees(angle):.2f} Grad')

    def get_info(self):
        return f'\u25b3ABC: side = {self.a}'