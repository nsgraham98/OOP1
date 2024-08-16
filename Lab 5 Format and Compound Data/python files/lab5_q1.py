mph = range(10, 71)

print(f"{"MPH":>3}{"KPH":>8}")

for mph in range(10, 71, 10):
    print(f"{mph:>3}{mph * 1.61:>8.1f}")
    

