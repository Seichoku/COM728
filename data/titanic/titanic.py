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
    print("[5] Display the number of survivors per age group")

    return int(input())


def display_passenger_name():
    print("The names of the passengers are...")
    for record in records:
        passenger_name = record[3]
        print(passenger_name)


def display_num_survivors():
    num_survived = 0
    for record in records:
        survival_status = int(record[1])
        if survival_status == 1:
            num_survived +=1
    print(f"{num_survived} passengers survived")


def display_passenger_per_gender():
    females = 0
    males =0
    for record in records:
        sex = record[4]
        if sex == "female":
            females += 1
        elif sex == "male":
            males += 1
    print(f"females: {females}, males: {males}")


def display_passenger_per_age_group():
    children = 0
    adults = 0
    elderly = 0
    for record in records:
        if record[5] != "":
            age = float(record[5])
            if age < 18:
                children += 1
            elif age < 65:
                adults += 1
            else:
                elderly += 1
    print(f"children: {children}, adults: {adults}, elderly: {elderly}")


def display_survivor_per_age_group():
    children = adults = elderly = 0
    children_survivor = adults_survivor = elderly_survivors = 0
    for record in records:
        survived = int(record[1])
        if record[5] != "":
            age = float(record[5])
            if age < 18:
                children += 1
                if survived == 1:
                    children_survivor += 1
            elif age < 65:
                adults += 1
                if survived == 1:
                    adults_survivor += 1
            else:
                elderly += 1
                if survived == 1:
                    elderly_survivors += 1

    print(f"children: {children_survivor}/{children}, adults: {adults_survivor}/{adults}, elderly {elderly_survivors}/{elderly}")


def run():
    load_data("titanic.csv")
    num_records = len(records)
    print(f"Successfully loaded {num_records} records.")
    selected_option = display_menu()
    print(f"You have selected option {selected_option}")
    if selected_option == 1:
        display_passenger_name()
    elif selected_option == 2:
        display_num_survivors()
    elif selected_option == 3:
        display_passenger_per_gender()
    elif selected_option == 4:
        display_passenger_per_age_group()
    elif selected_option == 5:
        display_survivor_per_age_group()
    else:
        print("you have selected an invalid option")


if __name__ == "__main__":
    run()
