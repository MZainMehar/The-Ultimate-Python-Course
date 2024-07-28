# Write a program using functions to find greatest of three numbers

def find_greatest():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))

    if num1 > num2 and num1 > num3:
        return num1
    
    elif num2 > num1 and num2 > num3:
        return num2
    
    else:
        return num3
    


greatest = find_greatest()

print(f"The greatest number is {greatest}")