import json


def read(file_path):
    with open(file_path) as file:
        data = json.load(file)
        city = data["city"]
        population = data["population"]
        name = data["name"]
        stat = data["stats"]
    print(f"City Name: {city}")
    print("City Name: {city_name}")