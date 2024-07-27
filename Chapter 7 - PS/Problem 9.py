# Write a program to print the following star pattern.
# * * *
# *   * 
# * * *

n = 3

for i in range(1, n + 1):
    if i == 1 or i == n:
        print("* " * n)
    else:
        print("*" + " " * (2 * n - 3) + "*") # first line: 2 * 1 - 3 = 1 space, second line: 2 * 2 - 3 = 1 space, third line: 2 * 3 - 3 = 3 spaces
