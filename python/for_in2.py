# val = {
#     "brand": "honda",
#     "type": "new",
#     "color": "green"
# }

# new_val = {}
# for k, v in val.items():
#     new_val[k] = v.upper()
# print(new_val)

# val = {
#     "brand": "honda",
#     "type": "new",
#     "color": "green"
# }

# new_val = {k: v.upper() for k, v in val.items()} 
# print(new_val)


# val = ["asd", "asdaa", "ss", "asdasd"]

# print(len(val[0]))

# new_val = []
# for elem in val:
#     if len(elem) <= 3:
#         new_val.append(elem)
# print(new_val)

val = ["asd", "asdaa", "ss", "asdasd"]
new_val = [elem for elem in val if len(elem) <= 3]

print(new_val)