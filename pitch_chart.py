# Exercise 10: Startup Pitch Deck Visualizer (ASCII Style)
# Draw a simple bar chart of projected revenue using # symbols.
 
# Projected revenue in millions for each year
revenue = [3, 5, 8, 12, 15]
 
print("Projected revenue by year ($ millions):")
 
year = 1
# Outer loop: one row for each year
for amount in revenue:
    print(f"Year {year}: ", end="")
 
    # Inner loop: print one # for each million
    for i in range(amount):
        print("#", end="")
 
    print(f" ({amount})")  # show the number and move to the next line
    year = year + 1