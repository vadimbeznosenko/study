"""
Изменить класс “Дробь” следующим образом:
- все статические свойства классов должны изменяться только внутри классовых методов;
- выделить один или несколько вспомогательных методов (если это не было сделано ранее)
и оформить их в виде статических методов.

"""
class Fraction():
    proper_fr_count = 0
    improper_fr_count = 0

    @classmethod
    def inc_fr_count(cls, is_proper):
        if is_proper:
            cls.proper_fr_count += 1
        else:
            cls.improper_fr_count += 1

    def set(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        Fraction.inc_fr_count(numerator < denominator)

    def print(self):
        print('\u0332'.join(f'{self.numerator}  '))
        print(f'{self.denominator}')

    def get_reversed(self):
        print('The reversed fraction of')
        self.print()
        print('is: ')
        rev_fr = Fraction()
        rev_fr.set(self.denominator, self.numerator)
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
            self.set(self.numerator//nod, self.denominator//nod)
            self.print()
        else:
            print('The fraction')
            self.print()
            print("can't be reduced!")


f1 = Fraction()
f1.set(5, 10)
f1.print()
f1.get_reversed()

f2 = Fraction()
f2.set(8, 3)
f2.print()

f3 = Fraction()
f3.set(5, 5)
f3.print()
f3.reduce()

f4 = Fraction()
f4.set(12, 36)
f4.print()
f4.reduce()

f5 = Fraction()
f5.set(3, 2)
f5.print()

print(f'Proper fractions count: {Fraction.proper_fr_count}')
print(f'Improper fractions count: {Fraction.improper_fr_count}'){"threads":[{"position":1089,"start":0,"end":1088,"connection":"closed"},{"position":1089,"start":1089,"end":2176,"connection":"open"}],"url":"https://att-b.udemycdn.com/2021-04-14_15-03-43-e62fca57529a91bb3d386ba79a075245/original.py?secure=v4xkH0AQqzPSgyvE8MXk1Q%3D%3D%2C1620281771&filename=1.py","method":"GET","port":443,"downloadSize":2176,"headers":{"date":"Thu, 06 May 2021 02:11:46 GMT","content-type":"text/x-python-script","content-length":"2176","connection":"close","x-amz-id-2":"EZM7f/ER6vyhNLW7dF8qu1a7sHo7pDX4/sKPeBxncgAdzo1uc91vGVa2y1ysncquXlKOUdUzY5k=","x-amz-request-id":"M5SGN9X2QY6X2XNH","last-modified":"Wed, 14 Apr 2021 15:03:44 GMT","etag":"\"f7823e8fdb07675b621061422f434a1b\"","x-amz-server-side-encryption":"AES256","x-amz-meta-qqfilename":"1.py","x-amz-version-id":"X0.hMKXi31hnLtVx_bp31zqWc9cNLZGj","x-77-nzt":"A7k73AFJIK6xubQOp+uoxLGP9DqBJimUwQ==","x-77-nzt-ray":"dV+o/SNMVb8=","x-77-cache":"MISS","cache-control":"max-age=31536000","content-disposition":"attachment; filename=\"1.py\"","x-cache-lb":"MISS, MISS","server":"CDN77-Turbo","x-77-pop":"frankfurtDE","accept-ranges":"bytes"}}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     