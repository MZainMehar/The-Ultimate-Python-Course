# Python function to print the random number between 1 and 100:

import random

def random_number():
    return random.randint(1, 100)


print(random_number())


# Second approach:

def random_number():
    return random.choice(range(1, 101))


print(random_number())