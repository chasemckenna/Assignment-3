# Exercise 7: Simple Supply Chain Tracker
# Add up the stock of each product across all warehouses.
 
warehouses = [
    {"name": "Warehouse A", "inventory": {"apples": 100, "bananas": 150}},
    {"name": "Warehouse B", "inventory": {"apples": 200, "bananas": 100}}
]
 
totals = {}  # will hold total stock for each product
 
# Outer loop: each warehouse
for warehouse in warehouses:
    inventory = warehouse["inventory"]
 
    # Inner loop: each product in that warehouse
    for product in inventory:
        if product in totals:
            totals[product] = totals[product] + inventory[product]
        else:
            totals[product] = inventory[product]
 
print("--- Total Stock Across Supply Chain ---")
for product in totals:
    print(f"{product}: {totals[product]}")
