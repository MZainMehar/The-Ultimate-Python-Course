# Some rules for naming variables in Python are as follows:

# 1. A variable name must start with a letter or the underscore character
_Age = 10 # valid
name = "John" # valid

# 2. A variable name cannot start with a number
# 1name = "John" # invalid

# 3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
name1 = "John" # valid
name_1 = "John" # valid

# 4. Variable names are case-sensitive (name, Name and NAME are three different variables)
name = "John" # valid
Name = "John" # valid
NAME = "John" # valid

# 5. The reserved words(keywords) cannot be used naming the variable. For example, False, class, finally, is, return, None, continue, for, lambda, try, True, def, from, nonlocal, while, and, del, global, not, with, as, elif, if, or, yield, assert, else, import, pass, break, except, in, raise
# False = 10 # invalid
# class = 10 # invalid
# is = 10 # invalid

# 6. Variable names should be descriptive and meaningful. For example, name is better than n, student_name is better than s_n, and name_length is better than length_of_name
n = "John" # not recommended and not so meaningful, instead use "name"
name = "John" # recommended and meaningful
# similarly
s_n = "John" # not recommended and not so meaningful, instead use "student_name"

# 7. Multiple words can be separated using an underscore. For example, student_name, student_age, and student_grade
studentname = "John" # not recommended, instead use "student_name"
student_name = "John" # recommended

# 8. Avoid using special characters like !, @, #, $, %, etc. in variable names
# student@name = "John" # invalid
# studentage! = 10 # invalid

# 9. Avoid using built-in functions as variable names. For example, print, input, type, int, str, etc.
# print = 10 # invalid
# str = 10 # invalid
# input = 10 # invalid
# type = "Hello" # invalid


