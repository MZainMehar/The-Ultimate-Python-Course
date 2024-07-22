# Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique.

my_dict = {}

for i in range(4):
    key = input("Enter you name: ")
    value = input("Enter your favourite language: ")
    my_dict[key] = value


print(my_dict)


