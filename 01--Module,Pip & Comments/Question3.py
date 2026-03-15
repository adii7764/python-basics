# Write a python program to print the contents of a directory using the os module. 
# Search online for the function which does that.  
import os

# specify the directory you want to list
directory_path = '/'

try:
    # list contents of the directory
    contents = os.listdir(directory_path)
    
    # print each item
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("Error: Directory not found!")
except PermissionError:
    print("Error: Permission denied!")
