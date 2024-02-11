# map_ = {
#     "speed": 400,
#     "time": 10,
#     "distance": 4000
# }

def route_info (route):
    if ("distance" in route) and (type(route["distance"]) == int):
        return f"Distance to your destination is {route['distance']}"
    if ("distance" not in route):
        return f"Distance to your destination is {route['time'] * route['speed']}"
    return "No distance is available "

print(route_info({'speed': 400, 'time': 10}))