# Slicing strings in Python is a way to extract a part of a string.

string = 'Hello_World'

print(len(string)) # Output: 11

new_string = string[0:6] # Extracts the first 6 characters of the string. Note that 6 is not included. It will print characters from index 0 to 5.

print(new_string) # Output: Hello_

new_string = string[6:] # Extracts all characters from index 6 to the end of the string.

print(new_string) # Output: World