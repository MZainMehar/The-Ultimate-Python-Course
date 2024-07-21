# Following are some operations that can be performed on sets:

# 1. add() - Adds an element to the set
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
my_set.add(11) # Adding an element to the set
print(my_set)


# 2.remove() - Removes the specified element from the set
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
my_set.remove(3) # Removing an element from the set
print(my_set)


# 3. len() - Returns the number of elements in the set
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(len(my_set))


# 4. clear() - Removes all the elements from the set
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
my_set.clear() # Removing all the elements from the set
print(my_set)

print(type(my_set))


# 5. pop() - Removes an arbitrary element from the set
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
my_set.pop() # Removing an arbitrary element from the set
print(my_set)


# 6. union() - Returns a set containing the union of sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.union(set2)

print(set3)

set = {1, 2, 3, 4, 5}
set.union({6, 7, 8, 9, 10}) 
print(set) # set remains unchanged why? because union() method returns a new set containing the union of the two sets.

# Now let's see how to update the set with the union of two sets
new_set = set.union({6, 7, 8, 9, 10}) 
print(new_set) # new_set contains the union of the two sets.


# 7. intersection() - Returns a set containing the intersection of sets
set1 = {1, 2, 3, 4, 5}
set2 = {1, 4, 3, 6, 7, 8}
set3 = set1.intersection(set2)
print(set3)

set4 = set1.union(set2)
print(set4)