# Creating new file and writing 
file_obj = open("test1.txt", mode="w")
file_obj.write("Welcome\nThis is a new text file")
file_obj.close()

file_obj2 = open("test1.txt", mode="r")

for line in file_obj2:
    print(line)