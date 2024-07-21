# Following are some of the methods of dictionary objects:

# 1. items() - Returns a list of key-value pairs

my_dict = {
    "fruit1" : "Apple",
    "fruit2" : "Banana",
    "fruit3" : "Cherry"
}

print(my_dict.items())


# 2. keys() - Returns a list of keys

my_dict = {
    "fruit1" : "Apple",
    "fruit2" : "Banana",
    "fruit3" : "Cherry"
}

print(my_dict.keys())


# 3. values() - Returns a list of values

my_dict = {
    "fruit1" : "Apple",
    "fruit2" : "Banana",
    "fruit3" : "Cherry"
}

print(my_dict.values())


# 4. get() - Returns the value of the specified key

my_dict = {
    "fruit1" : "Apple",
    "fruit2" : "Banana",
    "fruit3" : "Cherry"
}

print(my_dict.get("fruit2"))


# 5. update() - Updates the dictionary with the specified key-value pairs

my_dict = {
    "fruit1" : "Apple",
    "fruit2" : "Banana",
    "fruit3" : "Cherry"
}

my_dict.update({"fruit2" : "Date"})

print(my_dict)


# 6. pop() - Removes the element with the specified key

my_dict = {
    "fruit1" : "Apple",
    "fruit2" : "Banana",
    "fruit3" : "Cherry"
}

my_dict.pop("fruit2")

print(my_dict)


# 7. clear() - Removes all the elements from the dictionary

my_dict = {
    "fruit1" : "Apple",
    "fruit2" : "Banana",
    "fruit3" : "Cherry"
}

my_dict.clear()

print(my_dict)


# 8. copy() - Returns a copy of the dictionary

my_dict = {
    "fruit1" : "Apple",
    "fruit2" : "Banana",
    "fruit3" : "Cherry"
}

new_dict = my_dict.copy()

print(new_dict)


