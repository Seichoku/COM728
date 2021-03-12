import csv

records = []
headings = []


def load_data(file_path):
    print("Loading data.......")
    with open(file_path, "r") as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        for line in csv_reader:
            records.append(line)
       # num_records = len(records)
        #return num_records

    print("Done...")


def display_menu():
    print("Please select one of the following options:")
    print("[1] Display the names of all passengers")
    print("[2] Display the number of passengers that survived")
    print("[3] Display the number of passengers per gender")
    print("[4] Display the number of passengers per age group")

    return int(input())


def run():
    load_data("titanic.csv")
    num_records = len(records)
    print(f"Successfully loaded {num_records} records.")
    selected_option = display_menu()
    print(f"You have selected option {selected_option}")


run()