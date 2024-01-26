"""
Найти 2-ое, 6-ое и 11-ое по счету числа кратные 7, но не кратные 13 в диапазоне от 1000 до 2000.

--------------
Ответ: 1015, 1043, 1078
"""
ind = [2, 6, 11]
cur_ind = 0
res = []

for i in range(1000, 2001):
    if i % 7 != 0 or i % 13 == 0:
        continue
    cur_ind += 1
    if cur_ind in ind:
        res.append(i)
    if cur_ind == ind[-1]:
        break

print(res)