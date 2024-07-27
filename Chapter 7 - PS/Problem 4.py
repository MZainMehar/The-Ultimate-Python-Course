# Write a program to find whether a given number is prime or not.

number = int(input("Enter a number: "))

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")