# Functions with parameters are called with arguments. The function greet() has a parameter called name. When we call the greet() function, we pass an argument
#  we can use default arguments to call the function without passing any arguments.

# Functions with default arguments
def greet(name = "Stranger"):
    """This function greets to the person passed in as parameter"""
    print("Hello, " + name + ". Good morning!")

greet() # Function with default argument
greet('Paul') # Function with argument

# The parameter inside the function definition is called a default parameter. The default parameter is used when the function is called without passing any arguments.