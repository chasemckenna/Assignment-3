# Exercise 4: Sales Commission Calculator
# Calculate a 10% commission for each employee and rank them.
 
sales = {"Alice": 5000, "Bob": 7000, "Carol": 3000}
 
 
def calculate_commission(amount):
    """Return 10% of the sales amount."""
    return amount * 0.10
 
 
# Sort the names from highest sales to lowest
ranked_names = sorted(sales, key=sales.get, reverse=True)
 
print("--- Commission Leaderboard ---")
rank = 1
for name in ranked_names:
    commission = calculate_commission(sales[name])
    print(f"{rank}. {name}: ${commission:.2f}")
    rank = rank + 1
 