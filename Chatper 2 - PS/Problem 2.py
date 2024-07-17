#  Write a python program to find remainder when a number is divided by z.

number = int(input("Enter the number: "))
z = int(input("Enter the divisor: "))

remainder = number % z

print("The remainder when", number, "is divided by", z, "is: ", remainder)