# # example code

# grades = []
# grade = float(input("Enter a positive grade ('negative grade' to quit): "))
# while grade >= 0:
#     grades.append(grade)
#     grade = float(input("Enter next grade: "))
# print(f"You entered: {grades}")
# print(f'Average grade = {sum(grades)/len(grades)}')

#my code
grade = float(input("Enter a grade, (-ve to end): "))
grade_list = []

while grade >= 0 and grade <= 100:
    grade_list.append(grade)
    grade = float(input("Enter next grade: "))

grade_average = sum(grade_list)/len(grade_list)

print(f"Average of {grade_list} is {grade_average}")
