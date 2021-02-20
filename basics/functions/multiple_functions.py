def display_ladder(steps):
    for step in range(steps):
        print("| |\n***")

def create_ladder():
    print("Enter number of steps")
    steps = int(input())
    display_ladder(steps)
create_ladder()
