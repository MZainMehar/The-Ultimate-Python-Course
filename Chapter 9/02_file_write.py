str = "Hey there, I'm writing to a file!"
f = open('file.txt', 'w')
f.write(str)
f.close()

print("File written successfully!")

f = open('file.txt', 'r')
data=f.read()
print(data)
f.close()