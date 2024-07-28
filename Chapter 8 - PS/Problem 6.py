# Write a python function which converts inches to cms.

def inches_to_cms (inches):
    return inches * 2.54

inches = float(input("Enter the length in inches: "))
cms = inches_to_cms(inches)

print(f"The length {inches} inches is equeal to {cms} cms.")