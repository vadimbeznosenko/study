weather = [ { "temp": 34, "cloud": False, "water": "cool"}, 
           { "temp": 20, "cloud": True, "water": "Normal"}, 
           { "temp": 0, "cloud": True, "water": "Bad"} ]

summer, autumn, winter = weather

print(summer)
print(autumn)
print(winter)

def forcast (temp, cloud, water):
    return f"forcast for this day is temp {temp} it will be cloudly {cloud} and water is {water}"

print(forcast(summer["temp"], summer["cloud"], summer["water"]))