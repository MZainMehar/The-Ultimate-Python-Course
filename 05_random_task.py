import random

# Function to generate a random number 


def random_number(number):
    return random.choice(range(number))



def print_random_number(number):
    random_number = random.randint(0, number)
    print(random_number)


print(random_number(10))

print_random_number(100)





