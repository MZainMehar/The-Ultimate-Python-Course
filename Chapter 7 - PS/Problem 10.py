# Write a program to print multiplication table of n using for loops in reversed order.


n = int(input("Enter the value of n: "))

limit  = 10

for i in range(limit, 0, -1):
    print(f"{n} * {i} = {n * i}")