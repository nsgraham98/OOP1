import os
#Gets the current working drectory
cwd = os.getcwd()
print(cwd)

#Join paths
file_path = os.path.join(cwd, 'apple.txt')
print(file_path)

#checks if a file or directory exists
exists = os.path.exists(file_path)
print(exists)

#creates a new directory
os.mkdir('new_folder')
