# from json import load, dumps

# with open('./HiLeL_HW/HW.json', 'r') as json_data:
#     dict_data = load(json_data)


# for elem in dict_data.items():
#     list_dicts_data = elem[1]

# dict_data_name = [index_list["firstName"] for index_list in list_dicts_data]
# dict_data_lastname = [index_list["lastName"] for index_list in list_dicts_data]

# dict_data_json = dict(zip(dict_data_name, dict_data_lastname))

# with open('./HiLeL_HW/HW_result.json', 'w') as json_data:
#     dict_data = dumps(dict_data_json)

# print (dict_data_json)

nums =[1, 2, 3]
nums.insert(4,3)
print(nums)


    