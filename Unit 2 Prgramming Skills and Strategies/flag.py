counter = 0; total = 0
repeat_flag = True
while repeat_flag:
    grade = float(input("Enter grade (or negative value to end): "))
    if grade < 0:
        repeat_flag = False
    else:
        total += grade
        counter += 1
print("The average grade is", total / counter)
