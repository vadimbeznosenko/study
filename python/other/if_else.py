# my_img = ("1920", "1080")

# if len(my_img) == 2:
#     print(f"{my_img[0]}X{my_img[1]}")
# else:
#     print("Incorrect image formatting")

my_img = ("1920", "1080")
print(type(my_img[0]))
if (len(my_img) == 2) and (type(my_img[0]) == str and type(my_img[1]) == str):
    print(f"{my_img[0]}X{my_img[1]}")
else:
    print("Incorrect image formatting")