"""
Program which stores a quick menu of the combo meals for a friend's takeaway business.
Jade Akinbo
v6 - string checker, total prices
"""

import easygui

menu = \
{
    'Value' : {
        'Beef Burger' : '$5.69',
        'Fries' : '$1.00',
        'Fizzy Drink' : '$1.00',
        'Total Price' : '$7.69'
    },
    'Cheezy' : {
        'Cheeseburger': '$6.69',
        'Fries' : '$1.00',
        'Fizzy Drink' : '$1.00',
        'Total Price' : '8.69'
    },
    'Super' : {
        'Cheeseburger' : '$6.69',
        'Large Fries' : '$2.00',
        'Smoothie' : '$2.00',
        'Total Price' : '$10.69'
    }
}

def string_check(name):
    """Only allows names with letters and spaces, must be at least 4 letters
    long (excluding spaces)."""
    while True:
        name_stripped = name.replace(" ", "")
        if name_stripped.isalpha() and len(name_stripped) >= 4:
            return name.title()
        else:
            name = easygui.enterbox("Enter a valid name (letters and"
            " spaces only, min 4 letters):","Invalid Name")


def add_combo():
    """ Function which allows the user to add a new combo to the menu """

    input_combo_name = easygui.enterbox("Enter the combo name",
    "Combo Name")

    input_combo_name = input_combo_name.title()

    if input_combo_name in menu.keys():
        while input_combo_name in menu.keys():
            """ Simple loop to check whether the name the user chose for 
            their new combo is already on the menu """

            input_combo_name = input_combo_name.upper()

            easygui.msgbox(f"{input_combo_name} is already a combo "
                f"on the menu!", "Invalid Name Chosen")
            print("add combo: invalid - name taken\n") # print check

            input_combo_name = easygui.enterbox("Enter the combo name",
                "Combo Name")

            input_combo_name = input_combo_name.title()

            if input_combo_name not in menu.keys():
                print("add combo: valid - name not taken") # print check
                input_combo_name = input_combo_name.title()

            else: continue

    input_combo_name = string_check(input_combo_name)

    input_item_1 = easygui.enterbox("Enter the name of first item\nNote: "
    "\nWhen asked to list a price for an item, please exclude the dollar "
    "sign.","First Item")
    price_1 = easygui.integerbox("Enter a price for that Item",
    "Pricing")

    input_item_2 = easygui.enterbox("Enter the name of the second item",
    "Second Item")
    price_2 = easygui.integerbox("Enter a price for that Item",
    "Pricing")

    input_item_3 = easygui.enterbox("Enter the name of the third item",
    "Third Item")
    price_3 = easygui.integerbox("Enter a price for that Item",
    "Pricing")

    total_price = price_1 + price_2 + price_3

    price_1 = str(price_1)
    price_2 = str(price_2)
    price_3 = str(price_3)

    new_combo = {
        input_item_1.title(): '$' + price_1,
        input_item_2.title(): '$' + price_2,
        input_item_3.title(): '$' + price_3,
        'Total Price' : total_price
    }

    menu[input_combo_name] = new_combo

    print(input_combo_name)
    print()
    print(menu)

    """
    print(input_combo_name + " Combo")
    for key, value in new_combo.items():
        print(f"    {key}: {value}")
    """

    results = "\n".join([f"  {key}: {value}" for key, value in
    new_combo.items()])

    result_name = input_combo_name.title() + " Combo"
    easygui.msgbox(result_name + "\n"+results,"Combo Successfully Added!")

def search_combo(combo_name):
    """ Function for searching for an existing combo within the menu """
    for combo, combo_items in menu.items():
        if combo_name.title() in menu:
            print("search_combo(): name found")
            search_results = "\n".join([f"  {key}: {value}" for key, value in
            combo_items.items()])
            easygui.msgbox(combo_name.title() + " Combo" + "\n" +
            search_results,"Here are your search results")
            return # loop ends
    print("search_combo(): name not found")
    easygui.msgbox(f"Sorry, {combo_name.upper()} could not be found.",
    "Not Found")

def delete_combo(combo_name):
    """ Function which allows the user to delete a combo from the menu """
    if combo_name in menu:
        print(f"{combo_name} found") # confirm
        del menu[combo_name]
    if menu == {}:
        easygui.msgbox("There is nothing on the menu yet.",
        "Empty Menu")

def print_menu():
    for key, value in menu.items():
        print(f"  {key}: {value}")

    full_menu = "\n\n".join(["\n".join([f"{key}: {value}" for key,
    value in combo_info.items()])
    for combo_name, combo_info in menu.items()])
    easygui.msgbox(full_menu, "Full Burger Menu")

    return full_menu


""" Main Routine """

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
            name = easygui.enterbox("Please enter the name of the combo you "
            "would like to delete")
            name = name.title()

            delete_combo(name)

            full_list = "\n\n".join([combo_name + " Combo\n" + "\n".join([
            f"{key}: {value}" for key, value in combo_info.items()])
            for combo_name, combo_info in menu.items()])

            easygui.msgbox(full_list)
    else:
        # if the user decides to hit 'Exit'
        quit()