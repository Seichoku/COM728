def movement():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path


def test():
    print("Moving")
    path = movement()
    print(f"{path[0]} for {path[1]} steps")
    print(f"{path[2]} for {path[3]} steps")
    print(f"{path[4]} for {path[5]} steps")
    print(f"{path[6]} for {path[7]} steps")


if __name__ == "__main__":
    test()