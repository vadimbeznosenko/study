"""
Вычислить произведение последних трех чисел не кратных 5 в диапазоне от 20 до 50.

----------
47*48*49 = 110544
"""

res = 1
count = 0

for i in range(50, 19, -1):
    if i%5!=0:
        res *= i
        count += 1
    if count == 3:
        break

print(res)