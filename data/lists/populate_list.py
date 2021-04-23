def direction():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions


def menu():
    print("Please select a direction:")
    dirs = direction()
    for index in range(len(dirs)):
        dir = dirs[index]
        print(f"{index}: {dir}")
    index = int(input())
    return dirs[index]


def run():
    route = []
    print("Working out escape route....")
    for i in range(4):
        route.append(menu())
    print(f"Escape route: {route}")


if __name__ == "__main__":
    run()


if __name__ == "__main__":
    run()


