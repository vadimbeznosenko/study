list_1 = ["sport", "age", "speed"]
list_2 = ["backetboll", 23, 300]

def merge_list_to_dict (first_zip, second_zip):
    final_zip = zip(first_zip, second_zip)
    return final_zip

print(dict(merge_list_to_dict(first_zip=list_1, second_zip=list_2)))
print(dict(merge_list_to_dict(list_1, second_zip=list_2)))