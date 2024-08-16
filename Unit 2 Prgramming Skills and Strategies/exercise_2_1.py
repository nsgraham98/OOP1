# inputs 
current_price = int(input("Enter the current price:"))
last_month_price = int(input("Enter last month's price:"))

# calculations
price_difference = current_price - last_month_price
monthly_mortgage = (current_price * 0.051) / 12

# output
print("\nPrice Summary:")
print("Current Price: $",current_price)
print("Difference from last month: $",price_difference)
print("Monthly mortgage: $",monthly_mortgage)

