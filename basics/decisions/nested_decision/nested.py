print("What type of cover does the book have (hard / soft)")
book_type = input()
if book_type == 'soft':
    print("is the book is perfect bound ?")
    answer = input()
    if answer == 'yes':
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
else:
    print("Books with hard covers can be more expensive!")

