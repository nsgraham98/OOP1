def celsius_to_fahernheit(celsius):
    f = (9/5) * celsius + 32
    return f

def farenheit_to_celsius(farenheit):
    c = (farenheit - 32) * (5/9)
    return c

celsius_input = float(input("Enter your Celsius value to convert to Farenheit: "))
print(celsius_to_fahernheit(celsius_input))

farenheit_input = float(input("Enter your Farenheit value to convert to Celsius: "))
print(farenheit_to_celsius(farenheit_input))