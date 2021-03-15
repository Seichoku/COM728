import json


def read(file_path):
    print("Reading........")
    with open(file_path) as file:
        data = json.load(file)
    print("Done")
    return data


def save(file_path, data_save):
    print("Exporting......")
    with open(file_path, "w") as file:
        json.dump(data_save, file, indent = 4)

    print("Done")


def run():
    json_data = read("robocity.json")

    save("exported.json", json_data)


if __name__ == "__main__":
    run()


