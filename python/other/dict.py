
my_dict = dict()
key_dict1 = input(str("enter key1: "))
value_dict1 = input(str("enter value1: "))
key_dict2 = input(str("enter key1: "))
value_dict2 = input(str("enter value1: "))
key_dict3 = input(str("enter key1: "))
value_dic3 = input(str("enter value1: "))

my_dict[key_dict1] = value_dict1
my_dict[key_dict2] = value_dict2
my_dict[key_dict3] = value_dic3
print(dict(my_dict))

del my_dict[key_dict1]

print(my_dict)
