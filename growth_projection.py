
# Exercise 9: Business Growth Projection
# Project revenue for 10 years using a yearly growth rate.
 
revenue = float(input("Initial revenue: $"))
growth_rate = float(input("Growth rate (%): "))
 
print("\nYear | Revenue")
print("-----------------------")
 
for year in range(1, 11):
    revenue = revenue * (1 + growth_rate / 100)
    print(f"{year:>4} | ${revenue:,.2f}")
 
