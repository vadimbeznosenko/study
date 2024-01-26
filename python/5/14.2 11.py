"""
Создать базовый абстрактный класс “Array” (массив) с методами сложения и поэлементной обработки.

Определить производные классы “AndArray” и “OrArray”. В первом классе операция сложения реализуется
как пересечение множеств, а поэлементная обработка представляет собой извлечение квадратного корня.
Во втором классе операция сложения реализуется как объединение, а поэлементная обработка - вычисление логарифма.

* решите самостоятельно, какими свойствами будет обладать каждый из классов, и какие методы следует определить как абстрактные.

"""
from math import sqrt, log
from abc import ABC, abstractmethod


class Array(ABC):
    def __init__(self, *args):
        self.data = args

    @abstractmethod
    def plus(self, arr):
        pass

    @abstractmethod
    def edit_elem(self):
        pass


class AndArray(Array):
    def plus(self, arr):
        res = set(self.data).intersection(set(arr.data))
        print(f'Plus (intersection):\n{self.data} + {arr.data} = {tuple(res)}')
        return tuple(res)

    def edit_elem(self):
        res = list(map(sqrt, self.data))
        res = list(map(round, res, [2]*len(res)))
        print(f'Edit elements (sqrt):\n{self.data}  ->  {res}')
        return res


class OrArray(Array):
    def plus(self, arr):
        res = set(self.data).union(set(arr.data))
        print(f'Plus (union):\n{self.data} + {arr.data} = {tuple(res)}')
        return tuple(res)

    def edit_elem(self):
        res = list(map(log, self.data))
        res = list(map(round, res, [2] * len(res)))
        print(f'Edit elements (log):\n{self.data}  ->  {res}')
        return res


arr1 = AndArray(1,2,3,4,5,6,7,8,9)
arr2 = AndArray(3,6,8,0,2)
arr1.plus(arr2)
arr1.edit_elem()

print()

arr3 = OrArray(3,4,5,9,1,7,13)
arr3.plus(arr2)
arr3.edit_elem()