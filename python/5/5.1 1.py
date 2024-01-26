"""
Изменить класс “Дробь” следующим образом:
- добавить конструктор с выводом сообщения о том, что объект создан;
- добавить  инициализатор, в котором будут задаваться исходные значения объекта;
- добавить деструктор с выводом сообщения о том, что объект удален.
"""
class Fraction():
    proper_fr_count = 0
    improper_fr_count = 0

    def __new__(cls, *args, **kwargs):
        print("--This is constructor--")
        return super().__new__(cls)

    def __init__(self, numerator, denominator):
        print("--This is initializator--")
        self.numerator = numerator
        self.denominator = denominator
        Fraction.inc_fr_count(numerator < denominator)

    def __del__(self):
        print("--This is destructor--")

    @classmethod
    def inc_fr_count(cls, is_proper):
        if is_proper:
            cls.proper_fr_count += 1
        else:
            cls.improper_fr_count += 1

    def print(self):
        print('\u0332'.join(f'{self.numerator}  '))
        print(f'{self.denominator}')

    def get_reversed(self):
        print('The reversed fraction of')
        self.print()
        print('is: ')
        rev_fr = Fraction(self.denominator, self.numerator)
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
        nod = Fraction.get_nod(self.numerator, self.denominator)
        if nod != 1:
            print('The fraction')
            self.print()
            print('after reduction is: ')
            self.numerator //= nod
            self.denominator //= nod
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