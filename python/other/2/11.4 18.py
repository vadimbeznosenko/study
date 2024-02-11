"""
Дана квадратная матрица. Проверьте, является ли она диагональной.

------------
Тестовые значения:
[[2,0,0,0,0],
 [0,3,0,0,0],
 [0,0,5,0,0],
 [0,0,0,5,0],
 [0,0,0,0,2]]
"""

m = [[2,0,0,0,0],
     [0,3,0,0,0],
     [0,0,5,0,0],
     [0,0,0,5,0],
     [0,0,0,0,2]]

is_diag = True

for i in range(0, len(m)):
    for j in range(0, len(m[i])):
        if i != j and m[i][j] != 0:
            is_diag = False
            break

    if not is_diag:
        break

print(is_diag)