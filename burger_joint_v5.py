"""

Program which stores a quick menu of the combo meals for a friend's takeaway business.
Jade Akinbo
v5 - delete combo: allows user to delete a combo from the menu
   - print full menu: improvements
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

    (input_combo_name + " Combo")
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

def delete_combo(combo_name):
    """ Function which allows the user to delete a combo from the menu """
    if combo_name in menu:
        print(f"{combo_name} found") # confirm
        del menu[combo_name]
    if menu == {}:
        easygui.msgbox("There is nothing on the menu yet.", "Empty Menu")

def print_menu():
    full_menu = "\n\n".join(["\n".join([f"{key}: {value}" for key,
    value in combo_info.items()])
    for combo_name, combo_info in menu.items()])
    easygui.msgbox(full_menu, "Full Burger Menu")

    return full_menu


# Main Routine

"""Main Routine"""

while True:
    choice = easygui.buttonbox("Welcome, please choose an action",
    "Menu Options", choices=["Add Combo", "Search for a Combo",
        "Print Full Menu","Delete Combo", "Exit"])

    if choice == "Add Combo":
        add_combo()

    elif choice == "Search for a Combo":
        name = easygui.enterbox("Please enter the name of the combo you "
            "would like to search for")
        search_combo(name)

    elif choice == "Print Full Menu":
        full_menu = print_menu()

    elif choice == "Delete Combo":
            name = easygui.enterbox("Please enter the name of the combo you would "
            "like to delete")
            name = name.title()

            delete_combo(name)

            full_list = "\n\n".join([combo_name + " Combo\n" + "\n".join([
            f"{key}: {value}" for key, value in combo_info.items()])
            for combo_name, combo_info in menu.items()])

            easygui.msgbox(full_list)
    else:
        # if the user decides to hit 'Exit'
        quit()