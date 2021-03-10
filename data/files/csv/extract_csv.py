import csv


def extract(file_path):
    print("Extracting.......")
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        names = ""
        for line in csv_reader:
   #         print(line[1])
            names += f"{line[1]}\n"
    print("Done")
    print(f"The extracted values are \n{names}\n")


def run():
    extract("bots.csv")


if __name__ == "__main__":
    run()