def export(file_path,num_bot):
    print("Exporting....")

    with open(file_path, "a") as file:
        for count in range(num_bot):

            print("Enter bot id...")
            bot_id = int(input())

            print("Enter bot name...")git add
            bot_name = str(input())

            print("Enter bot paint...")
            bot_paint = str(input())

            file.write(f"{bot_id},{bot_name},{bot_paint}\n")
    print("Done")


def run():
    export("exported_bots.csv", 3)


if __name__ == "__main__":
    run()
