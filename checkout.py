# Exercise 1: Retail Checkout Simulation
# Keep asking for item prices until the user types 0.
 
prices = []  # empty list to hold the prices
 
price = float(input("Enter item price (0 to finish): "))
 
while price != 0:
    if price < 0:
        print("Price can't be negative. Try again.")
    else:
        prices.append(price)  # add the price to the list
    price = float(input("Enter item price (0 to finish): "))
 
# Calculate results
number_of_items = len(prices)
total = sum(prices)
 
print("\n--- Receipt ---")
print("Number of items:", number_of_items)
print(f"Total purchase: ${total:.2f}")
 
# Only find the average if at least one item was entered (avoid dividing by 0)
if number_of_items > 0:
    average = total / number_of_items
    print(f"Average item cost: ${average:.2f}")
else:
    print("No items were bought.")