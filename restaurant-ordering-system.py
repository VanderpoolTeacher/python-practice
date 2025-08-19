# # Define variables
#  
# Item number name of item price
# 1 Burger $5.99
# 2 Pizza $8.49
# 3 Salad $4.99
# 4 Drink $1.99

menu = {
    1 : {"name":"Burger","price":5.99},
    2 : {"name":"Pizza","price":8.49},
    3 : {"name":"Salad","price":4.99},
    4 : {"name":"Drink","price":1.99},
}

# initialize dictionary
order = {}

# # display welcome
# PRINT statement - WELCOME TO RESTAURANT
print("Welcome to Python Burger!")

# Initiate WHILE loop
order_total = 0

while True:
    # # display menu items
    #  Display menu items - (print statement) - for loop initiate menu_items
    
    print("Menu")
    for item_no, details in menu.items():
        print(f"{item_no}. {details['name']} - ${details['price']}")

    # # prompt menu selection
    # Prompt menu selection (user input)
    item_choice = int(input("Choose item: "))

    # # prompt qty
    # Prompt qty 
    item_qty = int(input("How many?"))

    # add order

    if item_choice in menu:
        item_name = menu[item_choice]['name']
    
        # Add or update item in order dictionary
        if item_name in order:
            order[item_name] += item_qty
        else:
            order[item_name] = item_qty

        # Optionally update total
        order_total += menu[item_choice]['price'] * item_qty
    else:
        print("Invalid item number.")

    print(order)