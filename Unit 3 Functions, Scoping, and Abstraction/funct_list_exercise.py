list = [8, 2, 0, 3, 7]

def sum_of_list(list):
    sum = 0
    for numbers in list:
        sum += numbers
    return sum

print(f"the sum of {list} is {sum_of_list(list)}")
