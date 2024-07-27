# Functions in Python is a block of code that only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
# A function is a group of related statements that perform a specific task.
# Functions help break our program into smaller and modular chunks. As our program grows larger and larger, functions make it more organized and manageable.
# It avoids repetition and makes the code reusable.
# Syntax:

# def function_name(parameters):
#     """docstring"""
#     statement(s)

# Above shown is a function definition that consists of the following components.
# 1. Keyword def that marks the start of the function header.
# 2. A function name to uniquely identify the function. Function naming follows the same rules of writing identifiers in Python.
# 3. Parameters (arguments) through which we pass values to a function. They are optional. 
# 4. A colon (:) to mark the end of the function header.
# 5. Optional documentation string (docstring) to describe what the function does.
# 6. One or more valid python statements that make up the function body. Statements must have the same indentation level (usually 4 spaces).
# 7. An optional return statement to return a value from the function.

# Example:
def greet(name):
    """This function greets to the person passed in as parameter"""
    print("Hello, " + name + ". Good morning!")

greet('Paul')