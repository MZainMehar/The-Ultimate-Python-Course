# Following are some methods that can be used with tuples:

# 1. count() - Returns the number of occurrences of the specified element.

tuple = (1, 2, 3, 4, 5, 3)
tuple.count(3) # Returns 2
print(tuple.count(3)) # 2


# 2. index() - Returns the index of the first occurrence of the specified element.

tuple = (1, 2, 3, 4, 5, 3)
print(tuple.index(3)) # 2


# 3. len() - Returns the number of elements in the tuple.

tuple = ('a', 'b', 'c', 'd', 'e')
print(len(tuple)) # 5


# 4. max() - Returns the largest element in the tuple.

tuple = (1, 2, 3, 4, 5)
print(max(tuple)) # 5


# 5. min() - Returns the smallest element in the tuple.

tuple = (1, 2, 3, 4, 5)
print(min(tuple)) # 1


# 6. sorted() - Returns a sorted list of the elements in the tuple.

tuple = (5, 4, 3, 2, 1)
print(sorted(tuple)) # [1, 2, 3, 4, 5]


# 7. sum() - Returns the sum of all elements in the tuple.

tuple = (1, 2, 3, 4, 5)
print(sum(tuple)) # 15


# 8. tuple() - Converts a list into a tuple.

# my_list = [1, 2, 3, 4, 5]
# my_tuple = tuple(my_list)
# print(my_tuple)  # (1, 2, 3, 4, 5)


