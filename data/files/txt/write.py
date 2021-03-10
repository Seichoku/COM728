def search(file_path):
    print("Searching......")
    sections = ""
    books = "Books:\n"

    with open("books.txt") as file:
        for line in file:
            if line.startswith("Section"):
                sections += line
            else:
                books += line
    print("Done!")

    return f"{sections}\n{books}"


def save(file_path, data):
    print("Saving....")
    with open("books.txt", "w") as file:
        file.write(data)
    print("Done")


def run():
    data = search("books.txt")
    save("books.txt", data)


run()

