def integer_ave_func(integer):
    count = 0
    integer_sum = 0
    while count <= integer:
        integer_sum += count
        count += 1
    ave_of_sum = integer_sum / integer
    print(f"The average of the sum of integers from 1 - {integer} is: {ave_of_sum}")

integer_ave_func(int(input("Enter an integer you'd like to find the average of the sum from 1 - [your integer]: ")))



