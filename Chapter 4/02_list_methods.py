# Following are some of the methods that can be used with lists:

# 1. append() - Adds an element to the end of the list.

list = [1, 2, 3, 4, 5]
list.append(6)
print(list)  # [1, 2, 3, 4, 5, 6]


# 2. sort() - Sorts the list in ascending order.

list = [5, 3, 1, 4, 2]
list.sort()
print(list) # [1, 2, 3, 4, 5]


# 3. reverse() - Reverses the order of the list.

list = [1, 2, 3, 4, 5]
list.reverse()
print(list) # [5, 4, 3, 2, 1]


# 4. insert() - Inserts an element at the specified index.

list = [1, 2, 3, 4, 5]
list.insert(2, 6) # Insert 6 at index 2
print(list) # [1, 2, 6, 3, 4, 5]


# 5. remove() - Removes the first occurrence of the specified element.

list = [1, 2, 3, 4, 5, 3]
list.remove(3) # Removes the first occurrence of 3
print(list) # [1, 2, 4, 5, 3]


# 6. pop() - Removes the element at the specified index.
list = [1, 2, 3, 4, 5]
list.pop(2) # Removes the element at index 2
print(list) # [1, 2, 4, 5]


# 7. clear() - Removes all elements from the list.
list = [1, 2, 3, 4, 5]
list.clear()
print(list) # []


# 8. copy() - Returns a copy of the list.
list = [1, 2, 3, 4, 5]
new_list = list.copy()
print(new_list) # [1, 2, 3, 4, 5]


# 9. count() - Returns the number of occurrences of the specified element.
list = [1, 2, 3, 4, 5, 3]
list.count(3) # Returns 2
print(list.count(3)) # 2


# 10. extend() - Adds the elements of another list to the end of the list.
list = [1, 2, 3, 4, 5]
list.extend([6, 7, 8])
print(list) # [1, 2, 3, 4, 5, 6, 7, 8]


# 11. index() - Returns the index of the first occurrence of the specified element.
list = [1, 2, 3, 4, 5, 3]
print(list.index(3)) # 2

