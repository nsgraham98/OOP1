def greeting():
    """This is called a doc string, used by the __doc__ command"""
    print("Hello, world!")

greeting()
print("=====================")

print(type(greeting))
print(greeting.__doc__)

for i in range(1,3):
    greeting()