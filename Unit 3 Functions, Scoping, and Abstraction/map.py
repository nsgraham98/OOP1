# map(function, iterable)
    # (iterable - list, tuple, dict, etc.)

# function - square
# iterable - new_list = [1, 2, 3, 4]

new_list = [1, 2, 3, 4]
def square(x):
    return x**2

squares = map(square, new_list)
print(list(squares))

#output: [1, 4, 9, 16]


