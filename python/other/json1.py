import json

product_1 = {
    "brand": "Honda",
    "price": 123,
    'available': True
}

json_product = json.dumps(product_1)
print(json_product)


dict_product = json.loads(json_product)
print(dict_product)