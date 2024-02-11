"""
Создать класс “Liquid” (жидкость) со свойствами: название и плотность жидкости, -
и методами: изменение плотности, вычисление объема жидкости, соответствующего заданной массе,
вычисление массы жидкости, соответствующей заданному объему, вывод информации о жидкости.

Создать производный класс “Alcohol” (спирт) с собственным свойством - крепость, - и методом:
изменение крепости.

Продемонстрировать работу класса-наследника и всех его методов.
"""
class Liquid:
    def __init__(self, name, density):
        self.name = name
        self.density = density

    def edit_density(self, val):
        self.density = val

    def calc_v(self, m):
        v = round(m / self.density, 2)
        print(f'The volume of {m} kg of {self.name} is {v} m^3.')
        return v

    def calc_m(self, v):
        m = v * self.density
        print(f'The weight of {v} m^3 of {self.name} is {m} kg.')
        return m

    def print_info(self):
        print(f'Liquid {self.name!r} (density = {self.density} kg/m^3).')


class Alcohol(Liquid):
    def __init__(self, name, density, strength):
        super().__init__(name, density)
        self.strength = strength

    def edit_strength(self, val):
        self.strength = val


a = Alcohol('Vine', 1064.2, 14)
a.print_info()

a.edit_density(1000)
a.print_info()

print()

a.calc_m(0.5)
a.calc_v(300)

print()

print(a.strength)
a.edit_strength(20)
print(a.strength)

