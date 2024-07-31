# Among the list, tuple, set and sictionary tuple is the only immutable data type. All other data types are mutable.
# This means that the data in the tuple cannot be changed, while the data in the other data types can be changed.
# This is the main difference between the tuple and the other data types.
# The tuple is created using the () brackets.
# To change the data in the tuple, you need to convert the tuple to a list, change the data, and then convert the list back to a tuple.
# You can create a tuple with a single element by adding a comma after the element.
# my_tuple = (1,) or my_tuple = 1, # Both are correct. 
# You can add two or more tuples by using the + operator.

# Example 1
# Create a tuple
tuple1 = (1, 2, 3, 4, 5)
print(tuple1)

# Convert the tuple to a list
list1 = list(tuple1)
print(list1)

# Change the data in the list
list1[0] = 10
print(list1)

# Convert the list back to a tuple
tuple1 = tuple(list1)
print(tuple1)

# However you can create a new tuple and add the data to the new tuple
tuple2 = (10, 2, 3, 4, 5)
print(tuple1 + tuple2)