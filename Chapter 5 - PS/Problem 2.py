# Write a program to input eight numbers from the user and display all the unique numbers (once).

# Creating a set

my_set = set()

for i in range(8):
    number = int(input("Enter a number: "))
    my_set.add(number)


print(my_set)