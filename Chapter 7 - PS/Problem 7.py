# Write a program to print the following star pattern.


n = 3

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1)) # first line: 2 * 1 - 1 = 1 star, second line: 2 * 2 - 1 = 3 stars, third line: 2 * 3 - 1 = 5 stars
