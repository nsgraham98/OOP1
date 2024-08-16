global_var = "im a global variable"

def outer_function():
    outer_var = "im in the outer scope"

    def inner_function():
        inner_var = "im in the inner scope"
        print("inner_var inside inner function", inner_var)
        print("outer_var inside inner function", outer_var)
        print("global_var inside inner function", global_var)

    inner_function()

outer_function()

print(global_var)