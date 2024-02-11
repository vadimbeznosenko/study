list_1 = [1, 3, 5, 2, 10, 8, 7, 6, 4, 9]
elem_max = max(list_1)
del_rith = list_1.index(elem_max)
del list_1[del_rith + 1:]
print(list_1)