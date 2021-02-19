print("Program Started")
print("Please Enter a Standard Character")
character = input()
if len(character) == 1:
    print(f"The ASCII code for {character} is {ord(character)}")
else:
    print("Enter a valid character and try again")
print("Program ended.")