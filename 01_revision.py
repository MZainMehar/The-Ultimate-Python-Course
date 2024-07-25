
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
my_list[0] = 7
my_list.insert(1, 2)
my_list.remove(6)
my_list.sort()


print(my_list) # [7, 2, 3, 4, 5, 6]


my_tuple = (1, 2, 3, 4, 5)
my_tuple = my_tuple + (6,)
# my_tuple = my_tuple[:1] + (2,) + my_tuple[1:]
print(sorted(my_tuple))
print(my_tuple) # (1, 2, 3, 4, 5, 6)


my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set) # {1, 2, 3, 4, 5, 6}