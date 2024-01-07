# Make a list of sandwich orders with 'pastrami' appearing at least three times
sandwich_orders = ["BLT", "Turkey Club", "Pastrami", "Veggie Wrap", "Chicken Parmesan", "Pastrami", "Pastrami"]

# Make an empty list for finished sandwiches
finished_sandwiches = []

# Print a message about running out of pastrami
print("Sorry, we're all out of pastrami.\n")

# Remove all occurrences of 'pastrami' from sandwich_orders using a while loop
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

# Loop through the list of sandwich orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# Print a message listing each sandwich that was made
print("\nList of Finished Sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
