# Recursive functions are functions that call themselves. They are used to solve problems that can be broken down into smaller, repetitive problems.

# Example:

def factorial(n):
    if (n == 0 or n == 1): # terminating condition, as soon as the value of n becomes 0 or 1, the function will return 1 and will not call itself again.
        return 1
    
    else:
        return n * factorial(n - 1) # first call: 3 * factorial(2) second call: 2 * factorial(1) third call: 1 * factorial(0)
    
fact = factorial(3)
print(fact)

# In recusrion you need to have a terminating condition, otherwise the function will call itself indefinitely.

# long_name = input("Enter a long name: ")
# short_name = long_name[0: 10]
# print(short_name)


# The programmer needs to be very careful while working with recursion as it can lead to an infinite loop if the terminating condition is not met.