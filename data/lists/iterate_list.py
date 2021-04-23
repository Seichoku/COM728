def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions


def menu():
    print("Please select a direction")
    path = directions()
    for index in range(len(path)):
        print(f"{index} is at  {path[index]}.")



def run():
    menu()



run()