def gang():
    print("Loading gang.....")
    friends = ["Scooby Doo", "Shaggy Rogers", "Fred Jones", "Dapne Blake", "Velma Dinkley"]
    print(friends)
    print("Done.")
    return friends


def phrase(friend):
    quotes = dict()
    friends = gang()
    for friend in friends:
        print(f"What does {friend} say??")
        quote = str(input())
        quotes[friend] = quote
    return quotes


def save(quote):
    friends = gang()
    quotes = phrase("Scooby Doo")

    with open("quotes.txt", "w") as file:
        for key, value in quotes:
            file.write(f"{key}: {value}")


save('Scooby')
print("The file contains...")
file = open("quotes.txt")
print(file.read())
file.close()