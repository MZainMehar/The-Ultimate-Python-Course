# Write a program which finds out whether a given name is present in a list or not.

name = input("Enter your name: ")

names = ["John", "Doe", "Jane", "Doe", "Alice", "Bob", "Charlie"]

if name in names:
    print("The given name is present in the list.")

else:
    print("The given name is not present in the list.")
    