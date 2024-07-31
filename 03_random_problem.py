# Different ways to print the sum of n natural numbers.

def sum_of_natural_numbers(n):

    sum = 0

    for i in range(1, n+1):
        sum += i

    return sum


print(sum_of_natural_numbers(5))


# Other ways to solve the problem:

def sum_of_natural_numbers(n):

    sum = 0 
    i = 1

    while (i<=n):
        sum += i
        i += 1

    return sum


print(sum_of_natural_numbers(5))