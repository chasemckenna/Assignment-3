# Exercise 8: Customer Loyalty Tiers
# Put each customer into a tier based on how much they spent.
 
customers = {
    "Alice": 750,
    "Bob": 1200,
    "Carol": 5600,
    "Dave": 300,
    "Eve": 4999,
    "Frank": 8000
}
 
bronze = 0
silver = 0
gold = 0
 
print("--- Customer Tiers ---")
for name in customers:
    amount = customers[name]
 
    if amount < 1000:
        tier = "Bronze"
        bronze = bronze + 1
    elif amount < 5000:
        tier = "Silver"
        silver = silver + 1
    else:
        tier = "Gold"
        gold = gold + 1
 
    print(f"{name}: ${amount} -> {tier}")
 
print("\n--- Summary ---")
print("Bronze customers:", bronze)
print("Silver customers:", silver)
print("Gold customers:", gold)
 
