# write a program which:
    # asks user for number of grades
    # gets grades from the user
    # calculates the average of grades
    # finds the maximum grade


max_grade = 0
grade_count = 0
grade_sum = 0

grade = float(input("Enter a grade, (enter negative value to stop)"))

while grade >= 0:
    grade_sum += grade
    grade_count += 1
    if grade > max_grade:
        max_grade = grade
    grade = float(input("Enter another grade,(enter negative value to stop)"))
    
average = grade_sum / grade_count

print("The average grade is:", average)
print("The largest grade is:", max_grade)