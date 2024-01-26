def image_info(img):
    if ('image_title' not in img) or ('image_id' not in img):
        raise TypeError ("not image id")
    return f"{img['image_title']}  has id {img['image_id']}"
print(image_info({'image_title': 'My cat', 'image_id': 123}))    
    
try:
    print(image_info({'image_id': 123}))
except TypeError as e:
    print(e)