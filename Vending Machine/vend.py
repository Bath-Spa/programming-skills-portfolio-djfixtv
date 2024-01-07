def display_products(products):
    # Print the ASCII art and product list
    print("                                           ___                _                         _          ")
    print("                                          / _ \\              | |                       | |         ")
    print("                                         / /_\\ \\ _ __   __ _ | | __  __ _  _ __  _   _ | |_   ___   ")
    print("                                         |  _  || '__| / _` || |/ / / _` || '__|| | | || __| / _ \\  ")
    print("                                         | | | || |   | (_| ||   < | (_| || |   | |_| || |_ | (_) |")
    print("                                         \\_| |_/|_|    \\__,_||_|\\_\\ \\__,_||_|    \\__,_| \\__| \\___/ ")
    print("                    ________________________________________________________________________________________________")
    print("                   |                                                                                                |")
    print("                   |         (A) - BITES          |          (B) - SWEETS         |         (C) - DRINKS            |")
    print("                   |------------------------------------------------------------------------------------------------|")
    # Product list with prices and codes
    print("                   | 1. Pocky Strawberry   - ¥130 | 1. Dorayaki            - ¥200 | 1. Yakult                - ¥40  |")
    print("                   | 2. Yan Yan            - ¥178 | 2. Dango               - ¥450 | 2. Ramune                - ¥90  |")
    print("                   | 3. Yamayoshi Chips    - ¥255 | 3. Ice Candy           - ¥255 | 3. Melon Soda            - ¥150 |")
    print("                   | 4. Koike-Ya Chips     - ¥113 | 4. Miso Butter Cookies - ¥650 | 4. Sake                  - ¥205 |")
    print("                   | 5. Calbee Pizza Chips - ¥215 | 5. Warabimochi         - ¥255 | 5. Milk Tea              - ¥350 |")
    print("                   | 6. Baum Rolls         - ¥290 | 6. Japanese Cheesecake - ¥1000| 6. Calpis                - ¥500 |")
    print("                   | 7. Lays Wasabi Chips  - ¥145 | 7. Mochi               - ¥786 | 7. Ice Tea               - ¥300 |")
    print("                   |================================================================================================|")
    # Instructions on how to Pay
    print("                   |                         THIS MACHINE ONLY ACCEPTS ¥100, ¥500 and ¥1000 BILLS                   |")
    print("                   |                          AN EXAMPLE OF HOW THE ITEMS ARE CHOSEN: (1A or 2B or 3C)              |")
    print("                   |                             *only UPPER case letters are accepted*                             |")
    print("                   |________________________________________________________________________________________________|")


def process_transaction(credits, product):
    # Get the price of the selected product
    price = product['price']

    while credits < price:
        try:
            additional_credits = float(input(f"Place Cash {price - credits}: "))
            credits += additional_credits
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    credits -= price
    # Print information about the selected product and remaining balance
    print(f"Product Selected: {product['name']}")
    print(f"Remaining Balance: {credits}")
    return credits


def vending_machine():
    # Product information with codes, names, and prices
    products = [
        {'product': '1A', 'name': 'Pocky Strawberry', 'price': 130},
        {'product': '2A', 'name': 'Yanyan', 'price': 178},
        {'product': '3A', 'name': 'Yamayoshi Chips', 'price': 255},
        {'product': '4A', 'name': 'Koike-Ya Chips', 'price': 113},
        {'product': '5A', 'name': 'Calbee Pizza Chips', 'price': 215},
        {'product': '6A', 'name': 'Baum Rolls', 'price': 290},
        {'product': '7A', 'name': 'Lays Wasabi Chips', 'price': 145},
        {'product': '1B', 'name': 'Dorayaki', 'price': 200},
        {'product': '2B', 'name': 'Dango', 'price': 450},
        {'product': '3B', 'name': 'Miso Butter Cookies', 'price': 650},
        {'product': '4B', 'name': 'Ice Candy', 'price': 255},
        {'product': '5B', 'name': 'Warabimochi', 'price': 255},
        {'product': '6B', 'name': 'Japanese Cheesecake', 'price': 1000},
        {'product': '7B', 'name': 'Mochi', 'price': 786},
        {'product': '1C', 'name': 'Yakult', 'price': 40},
        {'product': '2C', 'name': 'Ramune', 'price': 90},
        {'product': '3C', 'name': 'Melon Soda', 'price': 150},
        {'product': '4C', 'name': 'Sake', 'price': 205},
        {'product': '5C', 'name': 'Milk Tea', 'price': 350},
        {'product': '6C', 'name': 'Calpis', 'price': 500},
        {'product': '7C', 'name': 'Ice Tea', 'price': 300},
    
    ]

    # Initial credits
    credits = 0

    # Print the vending machine logo and initial product list
    print('                                                                           __  / __')
    print('                                                    |__| |  | |\/|  /\  | |  \  (_  ')
    print('                                                    |  | |__| |  | /--\ | |__/  __) ')
    print('                                            __       __          __               __              __ ')
    print('                                      \  / |_  |\ | |  \ | |\ | / _    |\/|  /\  /   |__| | |\ | |_  ')
    print('                                       \/  |__ | \| |__/ | | \| \__)   |  | /--\ \__ |  | | | \| |__ \n') 

    # Display product list
    display_products(products)

    while True:
        # Prompt user for product selection
        user_choice = input("What would you like to purchase? (Enter product code or 'q' to quit): ")

        if user_choice.lower() == 'q':
            break

        # Find the selected product based on the entered code
        selected_product = next((product for product in products if product['product'] == user_choice), None)

        if selected_product:
            # Process the transaction and update the credits
            credits = process_transaction(credits, selected_product)

            # Prompt user if they want to purchase more items
            purchase_another = input("Would you like to purchase anything else? (y/n): ").lower()
            if purchase_another != 'y':
                if credits != 0:
                    print(f"{credits} has been compensated!")
                    credits = 0
                print("Thank you for your purchase. Have a nice day!\n")
                break
        else:
            print("Invalid product code. Please try again.\n")


if __name__ == "__main__":
    vending_machine()
