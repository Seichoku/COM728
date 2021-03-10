def display_char(path, num_char):
    with open(path) as file:
        library = file.read(num_char)
        print("The first 20 Characters are:")
        print(library)


def display_line(path):
    with open (path) as file:
        line = file.readline().strip()
        print("The first line is:")
        print(line)


def display_text(path):
    with open(path) as file:
        library = file.read()
        print("The full text is:")
        print(library)


def run():
    display_char("library.txt", 15)
    display_line("library.txt")
    display_text("library.txt")


if __name__ == "__main__":
    run()
