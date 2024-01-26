list_1 = [1, 3, 5, 2, 10, 8, 7, 6, 4, 9]
elem_max = max(list_1)
del_rith = list_1.index(elem_max)
del list_1[del_rith + 1:]
print(list_1)

print("=" * 40)

list_1 = [1, 3, 5, 2, 10, 8, 7, 6, 4, 9]
elem_max = max(list_1)
elem_min = min(list_1)
del_rith = list_1.index(elem_max)
del_left = list_1.index(elem_min)
del list_1[del_left + 1:del_rith]
print(list_1)

print("=" * 40)

list_1 = [1, 3, 5, 2, 10, 8, 7, 6, 4, 9]
list_1.sort(reverse=True)
print(list_1)

print("=" * 40)

wrestling_club = ["Кругов Алексей", "Ворожейкин Борис", "Митин Сергей", "Алешин Сергей", 
                  "Кутиков Владимир", "Круглов Денис", "Бочкин Иван", "Мечников Алексей"]


wrestling_club.sort(reverse=False)

one = wrestling_club.count(" Сергей")

print(tuple(wrestling_club))