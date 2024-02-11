"""
Создать класс “Time” для работы со временем в формате Час:Минута:Секунда. Класс должен содержать:
- динамические свойства: количество часов, минут, секунд;
- статическое свойство: часовой пояс (строка в формате “UTC+/-число”);
- классовые методы: редактировать часовой пояс;
- статические методы: проверка корректности заданных величин (часов, минут, секунд),
перевод заданного значения из формата Час:Минута:Секунда в секунды и наоборот;
- конструктор: вызывает конструктор родительского класса и выводит сообщение о создании нового момента времени;
- инициализатор: проверяет корректность переданных величин, определяет динамические свойства класса и
выводит на экран информацию об объекте;
- деструктор: выводит сообщение о том, что момент времени удален;
- методы: вычисление разницы между двумя моментами времени в секундах, сложение с заданным количеством секунд,
вычитание заданного количества секунд, сравнение двух моментов времени, вывод на экран;

Продемонстрировать работу класса и всех его методов.
"""
class Time:
    pref = 'UTC'
    time_offset_min = -12
    time_offset_max = 14
    time_offset = 2
    time_offset_str = '{pref}{offset:+}'.format(pref=pref, offset=time_offset)

    def __new__(cls, *args, **kwargs):
        print('New timestamp was created.')
        return super().__new__(cls)

    def __init__(self, h, m, s):
        if Time.is_correct(h, m, s):
            self.h = h
            self.m = m
            self.s = s
            self.print_info()
        else:
            self.h = self.m = self.s = 0
            print('Wrong data!')
        print('-' * 50)

    def __del__(self):
        print(f'The timestamp {self.get_str()} was deleted!')

    @classmethod
    def edit_time_offset(cls, val):
        if cls.time_offset_min <= val <= cls.time_offset_max:
            cls.time_offset = val
            cls.time_offset_str = '{pref}{offset:+}'.format(pref=cls.pref, offset=cls.time_offset)
        else:
            print(f'Wrong value: the {cls.pref} time offset should be from '
                  f'{cls.time_offset_min:+} to {cls.time_offset_max:+} only!')

    @staticmethod
    def is_correct(h, m, s):
        return h in range(0, 24) and m in range(0, 60) and s in range(0, 60)

    @staticmethod
    def to_sec(h, m, s):
        return s + m * 60 + h * 3600

    @staticmethod
    def from_sec(sec):
        h = sec // 3600
        sec %= 3600
        m = sec // 60
        s = sec % 60
        return h, m, s

    def get_str(self):
        return f'{self.h:02}:{self.m:02}:{self.s:02} {Time.time_offset_str}'

    def print_info(self):
        print(f'The timestamp: {self.get_str()}')

    def calc_diff(self, timestamp):
        sec1 = Time.to_sec(self.h, self.m, self.s)
        sec2 = Time.to_sec(timestamp.h, timestamp.m, timestamp.s)
        res = sec2 - sec1
        print(f'The difference between {timestamp.get_str()} and {self.get_str()} is {res:+} sec.')

    def plus_sec(self, val):
        print(f'Add {val} sec to {self.get_str()}:')
        sec = Time.to_sec(self.h, self.m, self.s)
        sec += val
        self.h, self.m, self.s = Time.from_sec(sec)
        self.print_info()

    def minus_sec(self, val):
        print(f'Subtrack {val} sec from {self.get_str()}:')
        sec = Time.to_sec(self.h, self.m, self.s)
        sec -= val
        self.h, self.m, self.s = Time.from_sec(sec)
        self.print_info()

    def is_the_same_moment(self, timestamp):
        res = self.h == timestamp.h and self.m == timestamp.m and self.s == timestamp.s
        print(f'The timestamps {self.get_str()} and {timestamp.get_str()} '
              f'are {" not" if not res else ""} the same moments.')
        return res


t1 = Time(25, 18, 0)
t2 = Time(5, 89, 3)
t3 = Time(7, 13, 68)
print()

Time.edit_time_offset(100)
print(Time.time_offset_str)
print()

Time.edit_time_offset(-4)
print(Time.time_offset_str)
print()

t = Time(14, 5, 37)
t.print_info()
print()

t.calc_diff(Time(8, 0, 3))  # - 21 934 sec
t.plus_sec(320)     # + 5m 20s
t.minus_sec(3665)   # - 1h 1m 5s
print()

t.is_the_same_moment(Time(13, 9, 52))
t.is_the_same_moment(Time(13, 9, 53))
print()