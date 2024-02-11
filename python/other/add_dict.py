first_dict = {"brand": "Honda", "price": 7000}
second_dict = {"color": "red"}
next_dict = {"speed": 200}

final_dict = {
    **first_dict,
    **second_dict,
    **next_dict
}
print(final_dict)


# final_dict = first_dict | second_dict | next_dict
# print(final_dict)