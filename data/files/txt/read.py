def display_char(path, num_char):
    file = open(path)
    library = file.read(num_char)
    print("The first 20 Characters are:")
    print(library)
    file.close()


def display_line(path):
    file = open(path)
    line = file.readline().strip()
    print("The first line is:")
    print(line)
    file.close()


def display_text(path):
    file = open(path)
    library = file.read()
    print("The full text is:")
    print(library)
    file.close()


def run():
    display_char("library.txt", 15)
    display_line("library.txt")
    display_text("library.txt")


if __name__ == "__main__":
    run()
