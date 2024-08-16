# A dictionary is passed in
def printPrices(**kwargs):
    for productName, price in kwargs.items():
        print(f"The price of {productName} is {price:.2f}")

printPrices(ABC=11.95, widget=23.50, piano=4400.0)


print("=====================================")


def setup_dict(**kwargs):
    print(type(kwargs))
    return kwargs
cats_dict = setup_dict(cat1 = 'Dorian', 
                        cat2 = 'Huckleberry', 
                        cat3 = 'Winifred')
print(cats_dict)
