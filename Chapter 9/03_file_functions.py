# f = open('file.txt', 'r')

# lines = f.readlines()

# print(lines, type(lines))

# f.close()


f = open('file.txt', 'r')

line = f.readline()

while (line != ""):
    print(line)
    line = f.readline()

f.close()