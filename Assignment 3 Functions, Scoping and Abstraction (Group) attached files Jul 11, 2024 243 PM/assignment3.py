

def print_menu():
    isValid = False
    while isValid == False:
        print("\nSelect from the following options:")
        print("L- List Students")
        print("A- Add Student")
        print("E- Edit Student")
        print("D- Delete Student")
        print("F- Find A Student")
        print("G- GPA Average")
        print("Q- Quit")
        print("")
        menuItem = input("Enter the letter of your option: ").upper()
       
        validValues = "LAEDFGQ"
        if validValues.find(menuItem) >= 0:
            isValid = True
            print("You selected option ", menuItem, "\n")
        else:
            print("Invalid input. Please choose again.")
            print("")
   
    return menuItem

# find if a student is in file
# loads dictionary of students, checks to see if inputted id is in dictionary. prints result
def find_student():
    std_list = load_students()
    find_id = int(input("Enter student ID to find: "))
    print(f"Finding a student...\nsearching for student ID {find_id}")
    if find_id in std_list:
        for id, student_info in std_list.items():          
            if find_id == id:
                print("Student Found.")
                display_std_header()
                display_student(find_id)
    else:
        print("Student not found.")
         
# given id, name, gpa -> returns the student as a 2d dictionary {id: {name: gpa}}
def format_student(id, name, gpa):
    temp_dict = {}
    student_list = [id, name, gpa]

    outer_key_id = student_list[0]
    inner_key_name = student_list[1]
    value_gpa = student_list[2]

    if outer_key_id not in temp_dict:
        temp_dict[outer_key_id] = {}
        temp_dict[outer_key_id][inner_key_name] = value_gpa

    return temp_dict

# prints a header for the students
def display_std_header():
    print("=" * 75)
    print(f'{"Student ID":<} {"Student Name":>20} {"GPA":>13}')
    print("=" * 75)

# displays a single students info in a formatted string
# requires id value in argument
# loads the full dictionary and finds the item with the associated id, then prints it formatted with an fstring
def display_student(id):
    temp_dict = load_students() 

    for key, student_info in temp_dict.items():
        if id == key:
            for name, gpa in student_info.items():
                print(f'{id:<} {" ":>13} {name:<} {" " * (20 - len(name))} {gpa:<}')
    print("=" * 75)


# prints all the students 
# converts 2d dict to formatted string
def list_students():
    student_list = load_students()
    if len(student_list) < 1:
        print("Students list has no students.")
    else:
        display_std_header()
        for id, student_info in student_list.items():
            for name, gpa in student_info.items():
                print(f'{id:<} {" ":>13} {name:<} {" " * (20 - len(name))} {gpa:<}')
    print("=" * 75)
         

# checks if a student exists
# Asks for new student's info
# writes new student into the file
def add_student():
    try:
        with open('students.txt', 'r+') as f:
            ids = {line.split(",")[0] for line in f}
            id = input("Please enter the student ID: ")
            if id in ids:
                print("Student already exists with the given ID.")
            else:
                new_name = input("Please enter the student's name: ")
                new_GPA = input("Please enter the student's GPA: ")
                f.write(f"\n{id}, {new_name}, {new_GPA}")
                print(f"Student {new_name} added")
    except FileNotFoundError:
        print("File not found. Please ensure 'students.txt' exists.")
    

# edits a students info
# loads dictionary , finds if ID in dictionary, updates dictionary
# still needs to display updated student info with std_header
def edit_student():
    edit_std = int(input("Enter student ID to edit: "))
    std_list = load_students()
    
    if edit_std in std_list:
        print("Current student information: ")
        display_std_header()
        display_student(edit_std)
        for student in std_list:
            if student == edit_std:
                edit_std_name = input("Edit student name: ")
                edit_std_GPA = float(input("Edit student GPA: "))
                print("Student information updated Successfully.")
                temp_dict = (format_student(edit_std, edit_std_name, edit_std_GPA))
                std_list.update(temp_dict)
                update_students(std_list)
    else:
        print("Entered ID does not exist.")
        
          
    
# deletes student info 
# loads dictionary of students, finds if id exists in dictionary, deletes item related to id
def delete_student():
    temp_dict = load_students()
    id = int(input("Enter Student ID to delete: "))
    print("Deleting a student...")
    if temp_dict.get(id) is None:
        print("Student with given ID not found")
    else:
        del temp_dict[id]
        print("Student deleted successfully.")
        update_students(temp_dict)
    
# loads the dictionary of all student info, calculates average from gpa integer value
def calculate_average():
    temp_dict = load_students()
    total_gpa = 0
    count = 0
    for id, student_info in temp_dict.items():
        for name, gpa in student_info.items():
            total_gpa += gpa
            count +=1
    gpa_average = total_gpa/count
    print(f"Calculating GPA average...\nGPA Average: {gpa_average}")

# opens the text file, and converts it into a 2d dictionary
# returns 2d dictionary of all students
def load_students():
 
    file = open("students.txt", "r")
    line = file.readline().rstrip("\n")
    student_dict = {}
 
    while line != "":
        student_list = line.split(",")
        student_list[0] = int(student_list[0])
        student_list[2] = float(student_list[2])
 
        outer_key_id = student_list[0]
        inner_key_name = student_list[1]
        value_gpa = student_list[2]
 
        if outer_key_id not in student_dict:
            student_dict[outer_key_id] = {}
 
        student_dict[outer_key_id][inner_key_name] = value_gpa
 
        line = file.readline()
 
    file.close()
    return student_dict
      
# converts dictionary of students to string in text file
# requires full student dictionary as argument
def update_students(dict):
    temp_dict = dict
    with open('students.txt', 'w') as file:

        for id, student_info in temp_dict.items():
            for name, gpa in student_info.items():
                file.write(f"{id},{name},{gpa}\n")

def main():
    print("*" * 75)
    print(f'{" ":>13}"*** Welcome to the Students GPA System!***"')
    print("*" * 75)
    filename = input("Enter the filename of the students text file: ")
 
    try:
        with open(filename, 'r') as file:
            student_list = file.readlines()
            print(f"Loaded {len(student_list)} students from {filename}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return
 
    while True:
        choice = print_menu()
        if choice == 'L':
            list_students()
        elif choice == 'A':
            add_student()
        elif choice == 'E':
            edit_student()
        elif choice == 'D':
            delete_student()
        elif choice == 'F':
            find_student()
        elif choice == 'G':
            calculate_average()
        elif choice == 'Q':
            print("Quitting program. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose again.")

main()
