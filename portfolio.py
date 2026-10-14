# Exercise 5: Stock Portfolio Tracker
# Calculate the total value of a stock portfolio.
 
import random
 
portfolio = {
    "AAPL": {"shares": 10, "price": 170},
    "TSLA": {"shares": 4, "price": 250},
    "AMZN": {"shares": 2, "price": 130}
}
 
# Part 1: total value today
total_value = 0
for stock in portfolio:
    shares = portfolio[stock]["shares"]
    price = portfolio[stock]["price"]
    value = shares * price
    print(f"{stock}: {shares} shares x ${price} = ${value}")
    total_value = total_value + value
 
print(f"Total portfolio value: ${total_value:.2f}")
 
# Bonus: simulate one week of random price changes (between -5% and +5%)
print("\n--- One Week Simulation ---")
for day in range(1, 8):
    day_total = 0
 
    for stock in portfolio:
        change = random.uniform(-0.05, 0.05)  # random number from -0.05 to 0.05
        portfolio[stock]["price"] = portfolio[stock]["price"] * (1 + change)
        day_total = day_total + portfolio[stock]["shares"] * portfolio[stock]["price"]
 
    print(f"Day {day}: ${day_total:.2f}")