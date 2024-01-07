# Start the loop
while True:
    # Prompt the user to enter their age
    age_input = input("Enter your age (enter 'quit' to exit): ")

    # Check if the user wants to quit
    if age_input.lower() == 'quit':
        break  # Exit the loop if 'quit' is entered

    try:
        # Convert the user's input to an integer
        age = int(age_input)

        # Determine the ticket price based on age
        if age < 3:
            ticket_price = 0
        elif 3 <= age <= 12:
            ticket_price = 10
        else:
            ticket_price = 15

        # Print the cost of the movie ticket
        print(f"The cost of your movie ticket is ${ticket_price}.")
    except ValueError:
        print("Please enter a valid age or 'quit'.")
