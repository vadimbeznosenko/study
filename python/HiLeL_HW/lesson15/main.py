from json import dump

def some_func(list_a, list_b):
    some_dict1 = dict(zip(list_a, list_b))
    return some_dict1
    
def load_dict(some_dict, jsonpath):
    with open(jsonpath, 'w') as json_data:
       dump(some_dict, json_data)

list_a = [1,2,3,4,5]
list_b = [6,7,8,9,10]

some_var = some_func(list_a, list_b)

load_dict(some_var, jsonpath='./hw.json')


