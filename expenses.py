# Exercise 3: Expense Report Categorizer
# Add up expenses in each category, then the grand total.
 
expenses = {
    "Travel": [500, 200],
    "Meals": [40, 60, 30],
    "Supplies": [100]
}
 
grand_total = 0
 
print("===== Expense Summary Report =====")
 
# Outer loop: go through each category
for category in expenses:
    category_total = 0
 
    # Inner loop: go through each amount in that category
    for amount in expenses[category]:
        category_total = category_total + amount
 
    print(f"{category}: ${category_total}")
    grand_total = grand_total + category_total
 
print("----------------------------------")
print(f"Grand Total: ${grand_total}")