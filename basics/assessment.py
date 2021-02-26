def myth():
    print("Who wishes to learn about the demi god maui")
    name = str(input())
    print(f"{name}, he stole the heart of goddess Te Fiti")
    print("Now you must find Maui and lift the curse")


def explore(site):
    if site == 'The Cavern':
        print("You have found a camakau! You can sail the seas with this")
    else:
        print("This is just another part of the village")


def voyage(distance):
    for distance in range(distance):
        print("....Crossed some ocean")
    print("You have found Maui on an island!")


myth()
explore("Lagos")
explore("The Cavern")
voyage(6)
