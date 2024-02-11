
def route_info (route):
    if ("distance" in route) and (type(route["distance"]) == int ):
        return f"Distance to your destination is {route['distance']}"
    if ("distance" not in route):
        return f"Distance to your destination is {route['speed'] * route['time']}"
    return f"No Distance"
print(route_info({"time": 15, "speed": 15}))
    