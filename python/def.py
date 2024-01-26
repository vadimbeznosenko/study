

def merge_list_to_dict(first_zip, second_zip):
    final_zip = zip(first_zip, second_zip)
    return print(dict(final_zip))


first_zip = [1, 3, 6, 8, 11]
second_zip = [12, 15, 6, 8, 12]

merge_list_to_dict (first_zip, second_zip)