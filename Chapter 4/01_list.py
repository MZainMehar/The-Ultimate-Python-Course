# Lists are ordered collections of items that can be of different types.
# Lists are mutable, meaning they can be changed in place.
# Lists are defined by enclosing the elements in square brackets ([]).
# Elements are separated by commas.
# Lists can contain any Python object, including other lists.

friends = ["John", "Doe", "Alice", 5, 3.427, False, True]

print(friends[0])  # John

friends[0] = "grapes"

print(friends[0]) # grapes

print(friends[1:3]) # ['Doe', 'Alice']
