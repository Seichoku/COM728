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


def run():
    load_data("titanic.csv")
    num_records = len(records)
    print(f"Successfully loaded {num_records} records.")


run()