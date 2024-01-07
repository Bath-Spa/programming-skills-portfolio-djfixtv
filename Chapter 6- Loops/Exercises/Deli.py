# Make a list of sandwich orders
sandwich_orders = ["BLT", "Turkey Club", "Veggie Wrap", "Chicken Parmesan"]

# Make an empty list for finished sandwiches
finished_sandwiches = []

# Loop through the list of sandwich orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# Print a message listing each sandwich that was made
print("\nList of Finished Sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
