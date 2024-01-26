def update_car_info(**car):
    car["is_avalible"] = True
    return car

print(update_car_info (brand= "honda", price= 3000))