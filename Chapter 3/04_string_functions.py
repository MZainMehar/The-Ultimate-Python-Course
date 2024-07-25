# Following are some of the important string functions in Python:

# 1. len(): The len() function is used to get the length of a string. It returns the number of characters in the string.

string = 'Hello, World!'

print(len(string)) # Output: 13


# 2. endswith(): The endswith() function is used to check if a string ends with a specified suffix. It returns True if the string ends with the specified suffix, otherwise it returns False.

string = "Burj Khalifa"
string_ends_with = string.endswith("ifa")
print(string_ends_with) # Output: True

string_ends_with = string.endswith("Burj")
print(string_ends_with) # Output: False


# 3. startswith(): The startswith() function is used to check if a string starts with a specified prefix. It returns True is the string starts with the specified prefix, otherwise it returns False.

string = "Burj Khalifa"
string_starts_with = string.startswith("Burj")
print(string_starts_with) # Output: True

string_starts_with = string.startswith("khalifa")
print(string_starts_with) # Output: False


# 4. count(): The count() function is used to count the number of occurences of a substring in a string. It returns the number of times the substring appears in the string.

string = "Hello World"
string_count = string.count("l")
print(string_count) # Output: 3


# 5. find(): The find() function is used to find the index of the first occurence of a substring in a string. It returns the index of the first occurence of the substring in the string. If the substring is not found, it returns -1.

string = 'Hello, World!'
string_find = string.find('l')
print(string_find) # Output: 2

string_find = string.find('abc')
print(string_find) # Output: -1


# 6. rfind(): The rfind() function is used to find the index of the last occurence of a substring in a string. It returns the index of the last occurence of the substring in the string. If the substring is not found, it returns -1.

string = 'Hello, World!'
string_rfind = string.rfind('l')
print(string_rfind) # Output: 10


# 7. index(): The index() function is used to find the index of the first occurence of a substring in a string. It returns the index of the first occurence of the substring in the string. If the substring is not found, it raises a ValueError.

string = 'Hello, World!'
string_index = string.index('l')
print(string_index) # Output: 2

# string_index = string.index('abc')
# print(string_index) # Output: ValueError: substring not found


# 8. replace(): The replace() function is used to replace a substring with another substring in a string. It returns a new string with the specified substring replaced.

string = 'Hello, World!, Hello, World!'
new_string = string.replace('World', 'Universe')
print(new_string) # Output: Hello, Universe!


# 9. split(): The split() function is used to split a string into a list of substrings based on a delimiter. It returns a list of substrings.

string = 'Hello, World!'
string_split = string.split(',')
print(string_split) # Output: ['Hello', ' World!']


# 10. join(): The join() function is used to join a list of strings into a single string. It returns a single string.

string = 'Hello, World!'
string_split = string.split(',')
new_string = ''.join(string_split)
print(new_string) # Output: Hello World!


# 11. lower(): The lower() function is used to convert all characters in a string to lowercase. It returns a new string with all characters converted to lowercase.

string = "Hello, Universe!"
string_to_lower = string.lower()
print(string_to_lower) # Output: hello, universe!


# 12. upper(): The upper() function is used to convert all characters in a string to uppercase. It returns a new string with all characters converted to uppercase.

string = "Hello, Universe!"
string_to_upper = string.upper()
print(string_to_upper) # Output: HELLO, UNIVERSE!


# 13. strip(): The strip() function is used to remove leading and trailing whitespace characters from a string. It returns a new string with leading and trailing whitespace characters removed.

string = "   Hello, Universe!   "
string_stripped = string.strip()
print(string_stripped) # Output: Hello, Universe!


# 14. Capitalize(): The capitalize() function is used to convert the first character of a string to uppercase and the rest of the characters to lowercase. It returns a new string with the first character capitalized.

string = "hello, universe!"
string_capitalized = string.capitalize()
print(string_capitalized) # Output: Hello, universe!


# 15. title(): The title() function is used to convert the first character of each word in a string to uppercase and the rest of the characters to lowercase. It returns a new string with the first character of each word capitalized.

string = "hello, universe!"
string_title = string.title()
print(string_title) # Output: Hello, Universe!



