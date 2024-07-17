import os


directory_path = '/'

contents = os.listdir(directory_path)

for item in contents:
    print(item)

# This code snippet lists all the files and directories in the root directory of the system.