num = int(input("Input a whole number greater than 1: "))
num_count = 0
num_sum = 0

while num_count < num:
    num_count += 1
    num_sum += num_count

num_average = num_sum / num_count
print(num_average)