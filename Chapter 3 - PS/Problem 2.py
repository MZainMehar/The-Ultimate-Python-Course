# Write a program to fill in a letter template given below with name and date.

letter = '''Dear <|NAME|>,
You are selected!
<Date>'''

print(letter.replace("<|NAME|>", "John").replace("<Date>", "17/07/2024"))