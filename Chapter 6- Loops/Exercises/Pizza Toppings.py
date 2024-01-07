# Initialize an empty list to store pizza toppings
pizza_toppings = []

# Start the loop
while True:
    # Prompt the user to enter a pizza topping
    topping = input("Enter a pizza topping (enter 'quit' to finish): ")

    # Check if the user wants to quit
    if topping.lower() == 'quit':
        break  # Exit the loop if 'quit' is entered

    # Add the topping to the list and print a message
    pizza_toppings.append(topping)
    print(f"You'll add {topping} to your pizza.")

# Print the final list of pizza toppings
print("\nYour pizza will have the following toppings:")
for topping in pizza_toppings:
    print("- " + topping)
