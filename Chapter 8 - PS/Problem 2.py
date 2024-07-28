# Write a python program using function to convert Celsius to Fahrenheit.

# we use the C to F formula which is °F = (9/5) °C+32.

def C_to_F (C):
    F = (9/5) * C + 32
    return F


C = float(input("Enter the temperature in Celcius: "))

print(C_to_F (C))