"""
Задан список из 10 элементов. Изменить этот список таким образом,
чтобы все отрицательные элементы оказались в конце.
"""

l = [2, -5, -7, -3, -8, 4, 9, -1, 5, 7]

l.sort(reverse=True)
print(l)
