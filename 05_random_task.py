import random

# Function to generate a random number 


def random_number(number):
    return random.choice(range(number))



def print_random_number(number):
    random_number = random.randint(0, number)
    print(random_number)


print(random_number(10))

print_random_number(100)


# Function to print decimal/floating point number

def print_random_float():
    print(random.uniform(0, 100))

    # round off the number to 2 decimal places
    print(round(random.uniform(0, 100), 1))

    print(round(random.uniform(0, 100), 2))


print_random_float()




def print_random_float ():
    print(random.uniform(0, 100))

    print(round(random.uniform(0, 100), 1))

print_random_float()








