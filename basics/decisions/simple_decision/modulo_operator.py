print("Please enter a whole number")
num = int(input())
if num % 2 == 0:
    print("Number you have entered is even")
else:
    print("Number you have entered is odd")


def while_loop():
    print("How many bar should be charged:")
    bar_no = int(input())
    bars = 0
    while bars != bar_no:
        print(f"Charging: {'█'* bars} " )
        bars += 1

while_loop()