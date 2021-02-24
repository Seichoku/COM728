def display_in_box(word):
    box = len(word) + 3
    print('*' * box)
    print(f"{word}")
    print('*' * box)

def display_lower_case(word):
    print(f"{word.lower()}")

def display_upper_case(word):
    print(f"{word.upper()}")

def display_mirrored(word):
    mirrored = ""
    for letter in reversed(word):
        mirrored += letter
    print(f"{word} | {mirrored}")

def repeat(word):
    print("How many time would you like to repeat the word")
    cycle = int(input())
    for cycles in range(cycle):
        if cycle > 5:
            print(f"{word.lower()}")
        else:
            print(f"{word.upper()}")

def run():
    print("Please Enter a word")
    word = input()
    print("Please Select an options from the from 1-6 below")
    print("")
    print("1) Display in a Box")
    print("2) Display Lower")
    print("3) Display Upper")
    print("4) Display Mirrored")
    print("5) Repeat")
    print("6)Terminate Program")

    option = int(input())

    if option == 1:
        display_in_box(word)
    elif option == 2:
        display_lower_case(word)
    elif option == 3:
        display_upper_case(word)
    elif option == 4:
        display_mirrored(word)
    elif option == 5:
        repeat(word)
    elif option == 6:
        print("Program has been terminated")

run()