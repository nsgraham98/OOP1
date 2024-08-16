# my code
yesterday = 0.7588
today = 0.7479
change = yesterday - today

print(f"{"Date":>10}{"Rate":>10}")
print(f"{"=====":>10}{"=====":>10}")
print(f"{"Today:":>10}{today:>10}")
print(f"{"Yesterday:":>10}{yesterday:>10}")
print(f"{"Change:":>10}{change:>10.4f}")


# example code
# +9.2f means show the sign in a field 9 wide wih 4 digits after decimal point
# use "="*4
print(" ")

yesterday = 0.7588
today = 0.7479
change = today - yesterday

print("{:>9s} {:>9s}".format("Date", "Rate"))
print("{:>9s} {:>9s}".format("====", "===="))
print("{:>9s} {:+9.4f}".format("Yesterday", yesterday))
print("{:>9s} {:+9.4f}".format("Today", today))
print("{:>9s} {:+9.4f}".format("Change", change))
