"""
Program which stores a quick menu of the combo meals for a friend's takeaway business.
Jade Akinbo
v4 - print full menu
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
        input_item_1.title(): price_1,
        input_item_2.title(): price_2,
        input_item_3.title(): price_3
    }

    menu[input_combo_name] = new_combo

    print(input_combo_name + " Combo")
    for key, value in new_combo.items():
        print(f"    {key}: {value}")

def search_combo(combo_name):
    """ Function for searching for an existing combo within the menu """
    for combo, combo_items in menu.items():
        if combo_name.title() in menu:
            print("search_combo(): name found")
            search_results = "\n".join([f"  {key}: {value}" for key, value in
            combo_items.items()])
            easygui.msgbox(combo_name.title() + " Combo" + "\n" +
            search_results,"Here are your search results")
            return
    print("search_combo(): name not found")
    easygui.msgbox(f"Sorry, {combo_name.upper()} could not be found.",
    "Not Found")

# Main Routine

"""Main Routine"""

while True:
    choice = easygui.buttonbox("Welcome, please choose an action",
    "Menu Options", choices=["Add Combo", "Search for a Combo",
        "Print Full Menu", "Exit"])

    if choice == "Add Combo":
        add_combo()

    elif choice == "Search for a Combo":
        name = easygui.enterbox("Please enter the name of the combo you "
            "would like to search for")
        search_combo(name)

    elif choice == "Print Full Menu":
        full_list = "\n\n".join(["\n".join([f"{key}: {value}" for key,
        value in contact_info.items()])
         for contact_id, contact_info in
         menu.items()])
        easygui.msgbox(full_list, "Full Contact List")

    else:
        quit()