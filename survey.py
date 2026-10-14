# Exercise 2: Market Survey Analyzer
# Count how many customers chose each product and show market share.
 
responses = ["coffee", "tea", "coffee", "soda"]
 
counts = {}  # empty dictionary to store the counts
 
for drink in responses:
    if drink in counts:
        counts[drink] = counts[drink] + 1  # seen before, add 1
    else:
        counts[drink] = 1  # first time seeing it
 
total_people = len(responses)
 
print("--- Market Share ---")
for drink in counts:
    percent = counts[drink] / total_people * 100
    print(f"{drink}: {percent:.0f}%")