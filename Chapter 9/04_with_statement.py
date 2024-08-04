# With statement is used to open a file and automatically close it after the block of code is executed.
# It is a good practice to use with statement when working with files.

with open('file.txt', 'r') as f:
    lines = f.readlines()
    print(lines)
