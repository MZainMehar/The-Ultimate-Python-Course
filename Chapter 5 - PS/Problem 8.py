# If languages of two friends are same; what will happen to the program in problem 6?

# Solution:
# The program will work fine even if the languages of 2 friends are same.
# The dictionary will store the same value for the different keys.
# For example:

my_dict = {}

for i in range(4):
    key = input("Enter you name: ")
    value = input("Enter your favourite language: ")
    my_dict[key] = value


print(my_dict)


my_dict = {}

for i in range(4):
    key = input("Enter your name: ")
    value = input("Enter your marks: ")
    my_dict[key] = value


print(my_dict)