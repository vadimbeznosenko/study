# student = {
#     "name": "Ivan",
#     "id": "12321",
#     "car": "Honda",
#     "model": "civic",
#     "color": "red"
# }
# student.pop("id")
# student["new_key"] = "new_value"
# print(student)

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
