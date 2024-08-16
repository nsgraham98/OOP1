def student_grades():
    total_grade = 0
    num_of_students = 0

    i = open("student.txt", "r")
    for line in i:
        split_line = line.rstrip().split(",")
        name = split_line[0]
        grade = float(split_line[1])
        total_grade += grade
        num_of_students += 1
    i.close()

    total_grade_average = total_grade / num_of_students
    
    i = open("student.txt", "r")
    for line in i:
        split_line = line.rstrip().split(",")
        name = split_line[0]
        grade = float(split_line[1])
        if grade > total_grade_average:
            print(f"{name} : {grade}")
    i.close()

student_grades()

