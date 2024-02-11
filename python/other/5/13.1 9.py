"""
Внести изменения в созданный в первой задаче класс “Alcohol”:
переопределить методы вычисления массы и объема жидкости таким образом,
чтобы в них также рассчитывалось соответственно массовое или объемное содержание чистого спирта,
исходя из заданной крепости. Переопределить метод вывода информации о спирте.

Продемонстрировать работу измененных классов.
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
        self.strength = strength        # max = 1 (100%)

    def edit_strength(self, val):
        self.strength = val

    def calc_v(self, m):
        v = super().calc_v(m)
        v_alc = round(v * self.strength, 2)
        print(f'The volume of alcohol in {m} kg of {self.name} is {v_alc} m^3.')
        return v, v_alc

    def calc_m(self, v):
        m = super().calc_m(v)
        m_alc = round(m * self.strength, 2)
        print(f'The weight of alcohol in {v} m^3 of {self.name} is {m_alc} kg.')
        return m, m_alc

    def print_info(self):
        print(f'Liquid {self.name!r} (density = {self.density} kg/m^3, strength = {self.strength:.0%}).')


a = Alcohol('Vine', 1064.2, 0.14)
a.print_info()

a.edit_density(1000)
a.print_info()

print()

a.calc_m(0.5)
a.calc_v(300)

print()

a.print_info()
a.edit_strength(0.2)
a.print_info()

