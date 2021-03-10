def search(file_path):
    print("Searching........")
    with open("library.txt") as file:
        for location in file:
            print(f"looked in {location.strip()}")


def run():
    search("library.txt")


if __name__ == "__main__":
    run()
