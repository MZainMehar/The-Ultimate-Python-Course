# Can you change the values inside a list which is contained in set S?

# No we cannot change the values inside a list which is contained in set S. The set is an unordered collection of unique elements. The list is a mutable data type. If we change the values inside the list, the hash value of the list will change. As a result, the list will not be hashable anymore, and we will not be able to store it in the set.

# Let's see an example:

s = {8, 7, 12, "Harry", [1,2]}

# s[4][0] = 3 # Trying to change the value inside the list which is contained in set S

# print(s) # TypeError: unhashable type: 'list'
