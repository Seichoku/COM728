print("Please Enter first number")
first_num = int(input())
print("Please enter second number")
second_num = int(input())
print("Please Enter third number")
third_num = int(input())
odd = 0
even = 0
if first_num % 2 == 0:
   even = even + 1
else: odd = odd + 1
if second_num % 2 == 0:
   even = even + 1
else: odd = odd + 1
if third_num % 2 == 0:
   even = even + 1
else: odd = odd + 1

print(f"You have enter {even} even number(s) and {odd} odd number(s)")