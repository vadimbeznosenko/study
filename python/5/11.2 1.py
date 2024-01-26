"""
Создать класс “Account”, представляющий собой банковский счет. Класс должен содержать:
- динамические свойства: фамилия владельца, номер счета, процент начисления, сумма в рублях;
- статические свойства: курс рубля по отношению к доллару, курс рубля по отношению к евро;
- классовые методы: редактировать курс рубля по отношению к доллару, редактировать курс рубля по отношению к евро;
- статические методы: перевод суммы в доллары и евро;
- конструктор: вызывает конструктор родительского класса и выводит сообщение о создании нового банковского счета;
- инициализатор: определяет динамические свойства класса и выводит информацию об открытом счете;
- деструктор: выводит сообщение о том, что банковский счет закрыт;
- методы: смена владельца счета, снятие заданной суммы, начисление заданной суммы, начисление процентов,
перевод в доллары и евро (в отличие от аналогичных статических методов, данные методы не принимают параметров),
вывод информации о счете;

Продемонстрировать работу класса и всех его методов.
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
        self.num = num
        self.surname = surname
        self.percent = percent      # max=1 (100%)
        self.value = value
        print(f'The account #{self.num} owned by {self.surname} was opened.')
        print('*' * 50)

    def __del__(self):
        print('*' * 50)
        print(f'The account #{self.num} owned by {self.surname} was closed.')

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
        self.surname = surname

    def print_balance(self):
        print(f'The current balance is {self.value} {Account.suffix}')

    def withdraw_money(self, val):
        if val > self.value:
            print(f'Unfortunately, you have not {val} {Account.suffix}.')
        else:
            self.value -= val
            print(f'{val} {Account.suffix} was successfully withdrawed!')

        self.print_balance()

    def add_money(self, val):
        self.value += val
        print(f'{val} {Account.suffix} was successfully added!')
        self.print_balance()

    def add_percents(self):
        self.value += self.value * self.percent
        print('The percents was successfully added!')
        self.print_balance()

    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f'The current balance is {usd_val} {Account.suffix_usd}.')

    def convert_to_eur(self):
        eur_val = Account.convert(self.value, Account.rate_eur)
        print(f'The current balance is {eur_val} {Account.suffix_eur}.')

    def print_info(self):
        print('Account info:')
        print('-' * 20)
        print(f'#{self.num}')
        print(f'Owner: {self.surname}')
        self.print_balance()
        print(f'Percent: {self.percent:.0%}')
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

acc.withdraw_money(100)
print()

acc.withdraw_money(3000)
print()

acc.add_money(5000)
print()

acc.withdraw_money(3000)
print()