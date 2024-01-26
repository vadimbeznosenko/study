"""
Внести изменения в созданные классы следующим образом:
- динамические свойства класса “Time” должны иметь модификатор доступа protected;
- определить методы getter и setter для свойств с модификаторами доступа private и protected;
- любое взаимодействие с private и protected свойствами  должно производиться посредством соответствующих методов getter и setter.

Продемонстрировать работу измененных классов.
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
            self.set_h(h)
            self.set_m(m)
            self.set_s(s)
            self.print_info()
        else:
            self.set_h(0)
            self.set_m(0)
            self.set_s(0)
            print('Wrong data!')
        print('-' * 50)

    def __del__(self):
        print(f'The timestamp {self.get_str()} was deleted!')

    def set_h(self, h):
        self._h = h

    def get_h(self):
        return self._h

    def set_m(self, m):
        self._m = m

    def get_m(self):
        return self._m

    def set_s(self, s):
        self._s = s

    def get_s(self):
        return self._s

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
        return f'{self.get_h():02}:{self.get_m():02}:{self.get_s():02} {Time.time_offset_str}'

    def print_info(self):
        print(f'The timestamp: {self.get_str()}')

    def calc_diff(self, timestamp):
        sec1 = Time.to_sec(self.get_h(), self.get_m(), self.get_s())
        sec2 = Time.to_sec(timestamp.get_h(), timestamp.get_m(), timestamp.get_s())
        res = sec2 - sec1
        print(f'The difference between {timestamp.get_str()} and {self.get_str()} is {res:+} sec.')

    def plus_sec(self, val):
        print(f'Add {val} sec to {self.get_str()}:')
        sec = Time.to_sec(self.get_h(), self.get_m(), self.get_s())
        sec += val
        h, m, s = Time.from_sec(sec)
        self.set_h(h)
        self.set_m(m)
        self.set_s(s)
        self.print_info()

    def minus_sec(self, val):
        print(f'Subtrack {val} sec from {self.get_str()}:')
        sec = Time.to_sec(self.get_h(), self.get_m(), self.get_s())
        sec -= val
        h, m, s = Time.from_sec(sec)
        self.set_h(h)
        self.set_m(m)
        self.set_s(s)
        self.print_info()

    def is_the_same_moment(self, timestamp):
        res = self.get_h() == timestamp.get_h() \
              and self.get_m() == timestamp.get_m() \
              and self.get_s() == timestamp.get_s()
        print(f'The timestamps {self.get_str()} and {timestamp.get_str()} '
              f'are{" not" if not res else ""} the same moments.')
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