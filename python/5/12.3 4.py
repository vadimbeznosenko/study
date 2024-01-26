"""
Внести изменения в созданные классы следующим образом:
- динамические свойства класса “Account” должны иметь модификатор доступа private;
- определить методы getter и setter для свойств с модификаторами доступа private и protected;
- любое взаимодействие с private и protected свойствами  должно производиться посредством соответствующих методов getter и setter.

Продемонстрировать работу измененных классов.
"""
class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = 'RUB'
    suffix_usd = 'USD'
    suffix_eur = 'EUR'

    def __new__(cls, *args, **kwargs):
        print('New account was created successfully.')
        return super().__new__(cls)

    def __init__(self, num, surname, percent, value=0):
        self.set_num(num)
        self.set_surname(surname)
        self.set_percent(percent)   # max=1 (100%)
        self.set_value(value)
        print(f'The account #{self.get_num()} owned by {self.get_surname()} was opened.')
        print('*' * 50)

    def __del__(self):
        print('*' * 50)
        print(f'The account #{self.get_num()} owned by {self.get_surname()} was closed.')

    def set_num(self, num):
        self.__num = num

    def get_num(self):
        return self.__num

    def set_surname(self, surname):
        self.__surname = surname

    def get_surname(self):
        return self.__surname

    def set_percent(self, percent):
        self.__percent = percent

    def get_percent(self):
        return self.__percent

    def set_value(self, val):
        self.__value = val

    def get_value(self):
        return self.__value

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    def edit_owner(self, surname):
        self.set_surname(surname)

    def print_balance(self):
        print(f'The current balance is {self.get_value()} {Account.suffix}')

    def withdraw_money(self, val):
        if val > self.get_value():
            print(f'Unfortunately, you have not {val} {Account.suffix}.')
        else:
            self.set_value(self.get_value() - val)
            print(f'{val} {Account.suffix} was successfully withdrawed!')

        self.print_balance()

    def add_money(self, val):
        self.set_value(self.get_value() + val)
        print(f'{val} {Account.suffix} was successfully added!')
        self.print_balance()

    def add_percents(self):
        self.set_value(self.get_value() * (1 + self.get_percent()))
        print(f'The {self.get_percent():.0%} was successfully added!')
        self.print_balance()

    def convert_to_usd(self):
        usd_val = Account.convert(self.get_value(), Account.rate_usd)
        print(f'The current balance is {usd_val} {Account.suffix_usd}.')

    def convert_to_eur(self):
        eur_val = Account.convert(self.get_value(), Account.rate_eur)
        print(f'The current balance is {eur_val} {Account.suffix_eur}.')

    def print_info(self):
        print('Account info:')
        print('-' * 20)
        print(f'#{self.get_num()}')
        print(f'Owner: {self.get_surname()}')
        self.print_balance()
        print(f'Percent: {self.get_percent():.0%}')
        print('-' * 20)


acc = Account(num='12345', surname='Ivanov', percent=0.03, value=1000)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()

Account.set_usd_rate(2)
Account.set_eur_rate(3)
acc.convert_to_usd()
acc.convert_to_eur()
print()

acc.edit_owner(surname='Ivanova')
acc.print_info()
print()

acc.add_percents()
print()
acc.set_percent(0.05)
acc.add_percents()
print()

acc.withdraw_money(100)
print()

acc.withdraw_money(3000)
print()

acc.add_money(5000)
print()

acc.withdraw_money(3000)
print()