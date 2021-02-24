def play_guess_the_number():
    import random as rnd
    print("Please enter the minimum value")
    minimum = int(input())
    print("Please Enter the Maximum value")
    maximum = int(input())
    random_number = rnd.randrange(minimum, maximum)
    print(f"I am thinking of a number between {minimum} and {maximum}")
    print("Can you guess the Number?")
    correct = False

    while not correct:
        print("Enter a number")
        guess = int(input())
        if guess == random_number:
            print("You must be a side kick!! Congratulations you have guessed correctly")
            correct = True
        elif guess < random_number:
            print("Number is low")
        elif guess > random_number:
            print("Number is high")
        else:
            print("Try again")
    print("Game over")


play_guess_the_number()
