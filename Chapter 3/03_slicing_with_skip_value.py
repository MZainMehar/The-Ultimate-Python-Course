# Slicing with skip value means that you can skip a certain number of characters while slicing a string. 
# The syntax for slicing with skip value is string[start:stop:skip]. 
# The skip value is optional and is set to 1 by default. If you do not specify the skip value, it will slice the string with a skip value of 1. 
# If you specify a skip value of 2, it will skip every second character while slicing the string. If you specify a skip value of 3, it will skip every third character while slicing the string, and so on.

string = 'Hello_World'

new_string = string[0:11:2] # Extracts every second character from the string. It will print characters from index 0 to 10.

print(new_string) # Output: HloWrd