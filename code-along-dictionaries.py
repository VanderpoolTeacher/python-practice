# empty_dict = {}
# # print(type(empty_dict))

# product_prices = {
#     'creamer' : 3.79,
#     'apples' : 3.99,
#     'pears' : 3.99
# }

# product_keys = product_prices.keys()
# print(product_keys)

# product_values = product_prices.values()
# print(product_values)

# product_items = product_prices.items()
# print(product_items)

# look_for = 'apples' in product_prices
# print(look_for)

# menu = {
#     "Burger" : 5.99,
#     "Pizza" : 8.49,
#     "Salad" : 4.99,
#     "Drink" : 1.99
# }

# item_number = 1
# for item, price in menu.items():
#     print(f'{item_number}, {item}, ${price}')
#     item_number += 1

# global variables
menu = {
    1 : {"name":"Burger","price":5.99},
    2 : {"name":"Pizza","price":8.49},
    3 : {"name":"Salad","price":4.99},
    4 : {"name":"Drink","price":1.99},
}

order = {
    }

#functions
def print_menu():
    print("Menu")
    for item_no, details in menu.items():
        print(f"{item_no}. {details['name']} - ${details['price']}")

def prompt_menu_selection():
    # # prompt menu selection
    # Prompt menu selection (user input)
    item_choice = int(input("Choose item: " ))

    # # prompt qty
    # Prompt qty 
    item_qty = int(input("How many?" ))

#main program
while True:
    # # display menu items
    #  Display menu items - (print statement) - for loop initiate menu_items
    
    print_menu()

    prompt_menu_selection()

    # add order

    if item_choice in menu:
        item_name = menu[item_choice]['name']

        if item_name in order:
            order[item_name] += item_qty
        else:
            order[item_name] = item_qty

    else:
        print("That is not a valid menu item.")

    print(order)

    # continue ordering?
        # ask user do you want to continue adding to this order
    continue_order = input("Do you want to continue ordering? Y or N ").lower()
        # if yes, stay in loop
    if continue_order != 'y':
        break
        # if no, exit loop

# calculate total

# initialize variable, order_total - to store a float

# use a for loop to go over orders dictionary
    # set variable - item_price get item_price from menu dictionary (or orders if the price is included there)
    # get item_qty from orders dictionary
    # item_total = item_price * item_qty
    # print item_name, item_qty, item_total
    # add item_total to order_total
# print order_total