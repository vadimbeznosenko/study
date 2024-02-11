# def image_info (**car):
#     car["is_available"] = True
#     return print(car)
# update_car_info(brand="Honda", price= 2000)

def image_info(img):
    if ("image_id" not in img):
        raise TypeError("has not Image_id")
    elif ("image_title" not in img):
        raise TypeError("has not Image_title")
    return f"Image {img["image_id"]} has id {img["image_id"]}"
try:
    print(image_info({"image_id": "cat", "image_title": 123}))
except TypeError as e:
    print(e)