print("Toward which direction do you intend painting")
print("\n Please select from the options below:\n (a) up\n (b) down\n (c) left\n (d) right\n")
direction = str(input())
if direction == 'up':
    print("Painting Upward")
elif direction == 'down':
    print("Painting Downward")
elif direction == 'left':
    print("PaintingTowards the left")
elif direction == 'right':
    print("PaintingTowards the right")
else:
    print("You have not entered a valid option\n\nWould you like to retry??")