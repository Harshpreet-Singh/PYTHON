import os

# Specify the directory path; '.' refers to the current directory
# select the directory whose content you want to list
directory_path = '/'


# List all entries in the specified directory
# use the os module to list the directory entries/content
entries = os.listdir(directory_path)


# can use following both the methods to print the entries
# print(entries)
for entry in entries:
    print(entry)
