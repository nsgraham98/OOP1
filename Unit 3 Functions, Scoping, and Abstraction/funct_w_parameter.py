def student(first_name, last_name, student_id):
    print(first_name)
    print(last_name)
    print(student_id)
    print(f"Hello {first_name} {last_name}, your student ID is {student_id}")

student("nick", "graham", 956736)
student("joe", "smith", 123456)



def printLineOfChars(char, repeats):
    line = str(char) * repeats
    print(line)

printLineOfChars('-', 30)
printLineOfChars(1, 15)
