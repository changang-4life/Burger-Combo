"""Program which stores a quick menu of the combo meals for a friend's
takeaway business
Jade Akinbo
v2 - add_combo()
"""

import easygui

menu = \
{
    'Value' : {
        'Beef Burger' : '$5.69',
        'Fries' : '$1.00',
        'Fizzy Drink' : '$1.00'
    },
    'Cheezy' : {
        'Cheeseburger': '$6.69',
        'Fries' : '$1.00',
        'Fizzy Drink' : '$1.00'
    },
    'Super' : {
        'Cheeseburger' : '$6.69',
        'Large Fries' : '$2.00',
        'Smoothie' : '$2.00'
    }
}

def add_combo():
    """ Function which allows the user to add a new combo to the menu """
    input_combo_name = easygui.enterbox("Enter the combo name", "Combo Name")


    input_item_1 = easygui.enterbox("Enter the name of first item\nNote: When "
        "asked to list a price for an item, please exclude the dollar sign.",
        "First Item")
    price_1 = easygui.integerbox("Enter a price for that Item", "Pricing")


    input_item_2 = easygui.enterbox("Enter the name of the second item",
        "Second Item")
    price_2 = easygui.integerbox("Enter a price for that Item", "Pricing")


    input_item_3 = easygui.enterbox("Enter the name of the third item",
         "Third Item")
    price_3 = easygui.integerbox("Enter a price for that Item", "Pricing")

    new_combo = {
        input_item_1: price_1,
        input_item_2: price_2,
        input_item_3: price_3
    }

    menu[input_combo_name] = new_combo

    print(menu)

"""Main Routine"""

while True:
    choice = easygui.buttonbox("Welcome, please choose an action", "Menu Options",
        choices = ["Add Combo", "Exit"])

    if choice == "Add Combo":
        add_combo()

    else:
        quit()