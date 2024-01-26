"""
Изменить созданный ранее класс “Дробь” следующим образом:
- установить для одного из динамических свойств класса модификатор доступа protected,
а для остальных (если имеются) - модификатор доступа private;
- добавить соответствующие методы getter и setter.

"""
class Fraction():
    proper_fr_count = 0
    improper_fr_count = 0

    def __new__(cls, *args, **kwargs):
        print("--This is constructor--")
        return super().__new__(cls)

    def __init__(self, numerator, denominator):
        print("--This is initializator--")
        self.set_numerator(numerator)
        self.set_denominator(denominator)
        Fraction.inc_fr_count(numerator < denominator)

    def __del__(self):
        print("--This is destructor--")

    def get_numerator(self):
        return self._numerator

    def set_numerator(self, num):
        self._numerator = num

    def get_denominator(self):
        return self.__denominator

    def set_denominator(self, num):
        self.__denominator = num

    @classmethod
    def inc_fr_count(cls, is_proper):
        if is_proper:
            cls.proper_fr_count += 1
        else:
            cls.improper_fr_count += 1

    def print(self):
        print('\u0332'.join(f'{self.get_numerator()}  '))
        print(f'{self.get_denominator()}')

    def get_reversed(self):
        print('The reversed fraction of')
        self.print()
        print('is: ')
        rev_fr = Fraction(self.get_denominator(), self.get_numerator())
        rev_fr.print()

    @staticmethod
    def get_nod(a, b):
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a

    def reduce(self):
        nod = Fraction.get_nod(self.get_numerator(), self.get_denominator())
        if nod != 1:
            print('The fraction')
            self.print()
            print('after reduction is: ')
            self.set_numerator(self.get_numerator() // nod)
            self.set_denominator(self.get_denominator() // nod)
            self.print()
        else:
            print('The fraction')
            self.print()
            print("can't be reduced!")


f1 = Fraction(5, 10)
f1.print()
f1.get_reversed()

f2 = Fraction(8, 3)
f2.print()

f3 = Fraction(5, 5)
f3.print()
f3.reduce()

f4 = Fraction(12, 36)
f4.print()
f4.reduce()

f5 = Fraction(3, 2)
f5.print()

print(f'Proper fractions count: {Fraction.proper_fr_count}')
print(f'Improper fractions count: {Fraction.improper_fr_count}')