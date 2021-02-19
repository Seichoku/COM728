
def escape_by(plan):
    print("AAAAAHHHHH!!!!...... How do we Escape!!!...")
    print("We have 3 options, Select either 'a' 'b' or 'c'")
    print("a). jumping over\nb). running around\nc). going deeper\n")

    plan = input()
    if plan == 'a':
        print("We cannot escape that way! The boulder is too big!")
    elif plan == 'b':
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == 'c':
        print("That might just work! Let's go deeper!")
    else:
        print("We cannot escape that way! The boulder is too big!")

escape_by("a")
escape_by("b")
escape_by("c")