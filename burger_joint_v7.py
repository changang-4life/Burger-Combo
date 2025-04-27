"""
Program which stores a quick menu of the combo meals for a friend's takeaway business.
Jade Akinbo
v7 - edit_combo()
   - main, side and beverage functionality
   - more error checking: cancel button functionality
   - main routine is now a function
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
        if name is None: # user hits cancel while string checking
            main_routine() # goes back to start screen
        else:
            name_stripped = name.replace(" ", "")
            if name_stripped.isalpha() and len(name_stripped) >= 4:
                return name.title()
            else:
                name = easygui.enterbox("Enter a valid name (letters and"
                " spaces only, min 4 letters):","Invalid Name")

def add_combo():
    """ Function which allows the user to add a new combo to the menu """

    while True:
        input_combo_name = easygui.enterbox("Enter the combo name",
            "Combo Name")
        if input_combo_name is None:
            return # if user hits cancel, goes back to start screen
        else:
            input_combo_name = string_check(input_combo_name)
            break


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

    input_item_1 = easygui.enterbox("Enter the main course\nNote: "
    "\nWhen asked to list a price for an item, please exclude the dollar "
    "sign.","First Item")
    price_1 = easygui.integerbox("Enter a price for that Item",
    "Pricing")

    input_item_2 = easygui.enterbox("Enter the side",
    "Second Item")
    price_2 = easygui.integerbox("Enter a price for that Item",
    "Pricing")

    input_item_3 = easygui.enterbox("Enter the beverage",
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
        'Total Price' : f"${total_price:.2f}"
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
    if combo_name is None:
        main_routine()
    else:
        found = False
        search_term = combo_name.title()
        for combo, combo_items in menu.items():
            if combo == search_term:
                print("search_combo(): name found")
                search_results = "\n".join([f"  {key}: {value}" for key, value in
                combo_items.items()])
                easygui.msgbox(combo.title() + " Combo" + "\n" +
                search_results,"Here are your search results")
                found = True
                break  # Exit the loop once found
        if not found:
            print("search_combo(): name not found")
            easygui.msgbox(f"Sorry, {combo_name.upper()} could not be found.",
            "Not Found")

def delete_combo(combo_name):
    """ Function which allows the user to delete a combo from the menu """
    if combo_name in menu:
        print(f"\ndelete_combo: {combo_name} deleted") # confirm
        del menu[combo_name]
    if menu == {}:
        easygui.msgbox("There is nothing on the menu yet.",
        "Empty Menu")

def print_menu():
    """ Function which allows the user to show the full menu """
    for key, value in menu.items():
        print(f"  {key}: {value}")

    full_menu = "\n\n".join(["\n".join([f"{key}: {value}" for key,
    value in combo_info.items()])
    for combo_name, combo_info in menu.items()])
    easygui.msgbox(full_menu, "Full Burger Menu")

    return full_menu

def edit_combo(combo_name):
    """ Function which allows the user to edit details of a combo """
    component_choice = easygui.buttonbox("Please select which part of the "
        "combo you would like to edit", "Component Choice",
        choices=["Name", "Food / Drink", "Price"])

    og_combo = menu[combo_name]
    items = list(og_combo.items())

    if component_choice == "Name":
        while True:
            new_name = easygui.enterbox("Please enter a new name for the "
                f"{combo_name.upper()} combo", "Name Choice")
            new_name = string_check(new_name)
            new_name = new_name.title()

            confirm = easygui.buttonbox(f"Confirm changing the"
                f" {combo_name.upper()} combo to {new_name.upper()}",
                "Confirmation", choices=["OK", "Re-enter", "Cancel"])

            if confirm == "OK":
                menu[new_name] = menu[combo_name]
                del menu[combo_name]
                break
            elif confirm == "Re-enter":
                continue
            else: break

    elif component_choice == "Food / Drink":
        food_item = easygui.buttonbox("Please choose which food / drink "
            "in the combo you would like to change", "Item Choice",
            choices=["Main Course", "Side", "Beverage"])

        if food_item == "Main Course":
            part_chosen = "main course"
            old_key = items[0][0]
        elif food_item == "Side":
            old_key = items[1][0]
            part_chosen = "side"
        else:
            old_key = items[2][0]
            part_chosen = "beverage"

        og_combo = menu[combo_name]
        items = list(og_combo.items())

        new_food = easygui.enterbox(f"Please enter a new"
            f" {part_chosen.upper()} for the {combo_name.upper()} combo",
            f"{part_chosen.title()} - Name Choice")
        new_food = string_check(new_food)
        new_food = new_food.title()

        easygui.msgbox(f"Confirm changing the {part_chosen.upper()} for the"
            f" {combo_name.upper()} combo from {old_key.upper()} to"
            f" {new_food.upper()}")

        updated_combo = {}
        for key, value in og_combo.items():
            if key == old_key: # is this the key/food item we want to
                # rename?, i.e., is this 'beef burger'? - located via index

                updated_combo[new_food] = value # instead of the regular key
                # being added, the new main course name is added, along with
                # its regular value/price
            else:
                updated_combo[key] = value
                # key value pair that the iteration is up to gets added as
                # normal to the empty updated_combo dictionary

        menu[combo_name] = updated_combo # the whole combo dictionary is
        # replaced
        # by our new one

    else: # if they want to change a price
        food_item = easygui.buttonbox("Please choose "
            f"which food / drink in the {combo_name} combo you would like to "
            "change the price of", "Item Choice",
            choices=["Main Course", "Side", "Beverage"])

        if food_item == "Main Course":
            part_chosen = "main course"
            key = items[0][1]
            main_index = 0
        elif food_item == "Side":
            key = items[1][1]
            part_chosen = "side"
            main_index = 1
        else:
            key = items[2][1]
            part_chosen = "beverage"
            main_index = 2

        og_combo = menu[combo_name]
        items = list(og_combo.items())

        while True:
            new_price = easygui.enterbox(
                f"Please enter a new price for the {combo_name.upper()} "
                "combo","Pricing - Price Choice")
            try:
                new_price = float(new_price)
                break
            except:
                easygui.msgbox("Please enter a valid number with "
                    "or without decimals and no spaces","Invalid Input")

        new_price = str(new_price)

        easygui.msgbox(f"Confirm changing the {part_chosen} for the "
            f"{combo_name} combo from {key} to ${new_price:.2f}")

        items_list = []
        for key, value in og_combo.items():
            items_list.append(key)
            items_list.append(value)
        print(items_list)
        print(items)

        print(items[0][1])

        item_name = items[main_index][0] # gets name of selected item
        old_price = items[main_index][1] # gets old price attached to the item

        updated_combo = {}
        for key, value in og_combo.items():
            if key == item_name and value == old_price:
                print(f"old key: {key}")
                print(f"old value: {value}") # print checks

                updated_combo[key] = '$' + new_price # notes: instead of the
                # regular key being added, the new main course name is added,
                # along with its regular value/price
            else:
                updated_combo[key] = value
                # key value pair that the iteration is up to gets added as
                # normal to the empty updated_combo dictionary

        menu[combo_name] = updated_combo # the whole combo dictionary is
        # replaced by our new one

""" Main Routine """
def main_routine():
    while True:
        choice = easygui.buttonbox("Please choose an action",
            "Menu Options", choices=["Add Combo", "Search for a Combo",
            "Edit Combo", "Print Full Menu","Delete Combo", "Exit"])

        if choice == "Add Combo":
            add_combo()

        elif choice == "Search for a Combo":
            name = easygui.enterbox("Please enter the name of the combo you "
                "would like to search for")
            name = string_check(name)
            search_combo(name)

        elif choice == "Edit Combo":
            name = easygui.enterbox("Please enter the name of the combo you "
                "would like to edit", "Enter Name")
            name = string_check(name)

            if name.title() not in menu.keys():
                while name.title() not in menu.keys():
                    """ Simple loop to check whether the name the user chose for 
                    their new combo is already on the menu """

                    name = name.upper()

                    easygui.msgbox(f"{name} is not a combo on the menu!",
                        "Invalid Name Chosen")
                    print("edit combo: invalid - combo entered not on menu\n")
                    # print check

                    name = easygui.enterbox("Enter the combo name",
                        "Combo Name")
                    name = name.title()

                    if name in menu.keys():
                        print("edit combo: valid - name on menu ") # print check
                        name = name.title()

                    else: continue

            edit_combo(name)

        elif choice == "Print Full Menu":
            print_menu()

        elif choice == "Delete Combo":
                name = easygui.enterbox("Please enter the name of the "
                    "combo you would like to delete", "Delete Combo")
                name = string_check(name)
                delete_combo(name)

                full_list = "\n\n".join([combo_name + " Combo\n" + "\n".join([
                f"{key}: {value}" for key, value in combo_info.items()])
                for combo_name, combo_info in menu.items()])

                easygui.msgbox("Here is the new menu\n\n"+full_list,
                    "Updated Menu")
        else:
            # if the user decides to hit 'Exit'
            quit()

main_routine()