# the arg is a tuple that is passed in
def multiply(*args):
    product = 1
    for num in args:
        product *= num
    return product

print(multiply(2, 3, 7))
print(multiply(10,20))


def make_list(*args):
    print(args)
    list1 = [*args]
    list2 = list(args)

    print(list1, list2)
    
make_list('Mary', 'Mike', 'Anna')
