# student = {
#     "name": "Ivan",
#     "id": "12321",
#     "car": "Honda",
#     "model": "civic",
#     "color": "red"
# }
# student_list = list(student)
# index_first = student_list.pop(0)
# index_last = student_list.pop()
# insert_last = student_list.append(index_first)
# insert_first = student_list.insert(0, index_last)
# student_list_val = list(student.values())
# index_first_val = student_list_val.pop(0)
# index_last_val = student_list_val.pop()
# insert_last_val = student_list_val.append(index_first_val)
# insert_first_val = student_list_val.insert(0, index_last_val)
# dict_rev = zip(student_list, student_list_val)
# print(dict(dict_rev))
# student.pop(2)
# student["new_key"] = "new_value"


# student = {"name": "Emma", "class": 9, "marks": 75}
# print(student["marks"])

# p = {"name": "Mike", "salary": 8000} 
# print(p.get("age"))

# sample = {"1":["a","b"], "2":["c","d"]}
# print(sample["2"][1])

# list_1 = ["Украина-Киев", "Россия-Сочи", "Беларусь-Минск", "Япония-Токио", "Германия-Мюнхен"]
# list_2 = ["Киев", "Токио", "Минск"]
# dict_ = dict()
# dict_["Украина"] = list_2[0]
# dict_["Япония"] = list_2[1]
# dict_["Беларусь"] = list_2[2]
# print(dict_)

# user_input = list(input("Enter for cript value: "))
# list_1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# dict_ = dict()
# for val in range(0, 26):
#     dict_[list_1[val]] = val
# for k in user_input:
#     print(dict_[k], end='')

# dict_ = dict()
# for val in range(1, 10):
#     dict_[val] = val ** 2
# print(dict_)
# dict_ = {val: val ** 2 for val in range(1, 10)}
# print(dict_)

# list_1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# dict_ = dict()
# for val in list_1:
#     cunt = list_1.index(val)
#     dict_[cunt] = val
# print (dict_)
