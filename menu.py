# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola Bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai Iced": 3.99,
            "Irish Breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat White": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate Lava Cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice Pudding": 4.99,
        "Fried Banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            menu_selection = input("Type item number: ")

            # 3. Check if the customer typed a number
            if menu_selection .isdigit():
            
                # Convert the menu selection to an integer
                menu_selection = int(menu_selection)
                # 4. Check if the menu selection is in the menu items
                if menu_selection not in menu_items.keys():
                    
                    print("Input Error")
                    continue

                elif menu_selection in menu_items.keys():

                    # Store the item name as a variable

                    menu_selection_name = menu_items[menu_selection]["Item name"]

                    # Ask the customer for the quantity of the menu item
                    quantity = input(f"How many {menu_selection_name} would you like to order? (Enter 1 or blank for 1):  ")

                    # Check if the quantity is a number, default to 1 if not
                    if quantity .isdigit(): 
                        quantity = int(quantity)
                    else:
                        quantity = 1

                    # Add the item name, price, and quantity to the order list
                    order.append(
                        { "Item name" : menu_selection_name,
                          "Price"     : menu_items[(menu_selection)]["Price"],
                          "Quantity"  : quantity
                        }
                    )
                    # Tell the customer that their input isn't valid
            else: print("You have entered an invalid selection.") 
                # Tell the customer they didn't select a menu option
        else:
            print("You have selected an invalid category.")
            # Tell the customer they didn't select a menu option
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o?")

        # 5. Check the customer's input
        match keep_ordering.strip().upper():
            case 'Y':  

                # Keep ordering
                place_order = True
                
                # Exit the keep ordering question loop
                break
                
                # Complete the order
            case 'N':
                place_order = False
                # Since the customer decided to stop ordering, thank them for their order
                print("Thank you for your order.")
                # Exit the keep ordering question loop
                break
                # Tell the customer to try again
            case _:
                print("Please try again.")
                continue

# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
for orders in order:
    for key, value in orders.items():
    # 7. Store the dictionary items as variables
        if key == 'Item name':
            item_name = value
            
        elif key == 'Price':
            price = value
            
        elif key == 'Quantity':
            quantity = value

    # 8. Calculate the number of spaces for formatted printing
    num_item_spaces = 26 - len(item_name)
    num_price_spaces = 8 - len(str(price))
    num_qty_spaces = 10 - len(str(quantity))

    # 9. Create space strings
    receipt_item_spaces = " " * num_item_spaces
    receipt_price_spaces = " " * num_price_spaces
    receipt_qty_spaces = " " * num_qty_spaces

    # 10. Print the item name, price, and quantity
    print(f"{item_name} {receipt_item_spaces} {price} {receipt_price_spaces} {quantity} {receipt_qty_spaces}")
    
# 11. Calculate the cost of the order using list comprehension
    order_cost = 0

# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.

    order_cost = sum(item['Price'] * item['Quantity'] for item in order)

print("\n")
print(f'Your order total comes to {order_cost}.')