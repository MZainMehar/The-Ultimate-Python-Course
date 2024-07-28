# Write a python function to remove a given word from a list ad strip it at the same time.

def remove_word(word):
    my_list = ["Alice", "Bob", "Charlie", "David", "Eve"]
    my_list.remove(word)
    # my_list.strip(" ") 
    return my_list


print(remove_word("Charlie"))
