import os

# Set the directory path you want to list
directory_path = '/'

# List all the files and directories in the specified path
contents = os.listdir(directory_path)

# Print the list of files and directories
for item in contents:
    print(item)

# This code snippet lists all the files and directories in the root directory of the system.