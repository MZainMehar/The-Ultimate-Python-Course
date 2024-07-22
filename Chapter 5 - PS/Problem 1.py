# Write a program to create a dictionary of Urdu words with values as their English translation. Provide user with an option to look it up!

# Creating a dictionary

my_dictionary = {
    "سیب" : "Apple",
    "کیلا" : "Banana",
    "چیری" : "Cherry",
    "کھجور" : "Date",
    "سمبل" : "Elderberry",
    "انجیر" : "Fig",
}

print("Enter the Urdu word to get its English translation: ")
word = input()

print(my_dictionary.get(word, "Word not found!"))