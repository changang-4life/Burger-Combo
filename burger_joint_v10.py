"""
Program which stores a quick menu of the combo meals for a friend's takeaway business.
Jade Akinbo
v10 trialling 2: Delete Combo
- Added confirmation so the user doesn't accidentally delete a combo they
didn't want to
- if user enters a name that is not on the dictionary, they can choose to
either enter again or go back to the start screen
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

def values_check(price, name, component):
    if not name:
        while True:
            if price is None:
                main_routine()
            else:
                try:
                    float(price)
                    return price
                except ValueError:
                    price = easygui.enterbox("Please enter a valid price"
                        f" for the {component}\nMake sure you do not include "
                        "the '$' symbol in your prices","Invalid Price")
                    continue

    elif not price:
        while True:
            if name is None:
                main_routine()
            else:
                name_stripped = name.replace(" ", "")
                if name_stripped.isalpha() and 3 <= len(name) <= 30:
                    # if name is completely a string and its length is equal to or
                    # more than 3, the name is considered valid
                    return name.title()
                else:
                    name = easygui.enterbox(f"Please enter a valid name "
                        f"for the {component}\nMake sure it is from 3 - 30 "
                        f"characters long", "Invalid Name")
                    # else, the loop asks them to input a valid name
                    continue

def string_check(name):
    """ Only allows names with letters and spaces, must be at least 3 letters
    long (excluding spaces) """

    while True:
        if name is None: # user hits cancel while string checking
            main_routine() # goes back to start screen
        else:
            name_stripped = name.replace(" ", "")
            if name_stripped.isalpha() and 3 <= len(name_stripped) <= 30:
                return name.title()
            else:
                name = easygui.enterbox("Enter a valid name\n(Letters and"
                " spaces only, min 3 letters, max 30 letters)",
                "Invalid Name")

def add_combo():
    """ Function which allows the user to add a new combo to the menu """

    dessert_choice = easygui.buttonbox("Would you like to add a dessert"
        f" to your new combo?", "Add Combo", choices=["Yes", "No"])


    fields = ["Combo Name", "Main Course", "Price", "Side", "Price",
            "Beverage", "Price"] # no dessert

    if dessert_choice == "Yes":
        fields = ["Combo Name", "Main Course", "Price", "Side", "Price",
            "Beverage", "Price", "Dessert", "Price"]

        values = easygui.multenterbox("Enter combo details",
            "Add Combo", fields)

        if values is None:
            print(type(values))
            print("value is None (if block 1)")
            main_routine()

        if '' in values:
            while '' in values:
                print(type(values))
                easygui.msgbox("Please enter information in all the "
                    "fields or cancel to go back to the start screen.",
                    "Invalid Input(s)")
                values = easygui.multenterbox("Enter combo details",
                    "Add Combo", fields)
                if values is None:
                    print(type(values))
                    print("value is None (last if block)")
                    main_routine()
            print(values)

        (input_combo_name, input_item_1, price_1, input_item_2, price_2,
         input_item_3, price_3, input_item_4, price_4) = values

        input_combo_name =  values_check(False, input_combo_name,
            "combo")
        input_item_1 = values_check(False, input_item_1,
            "main course")
        input_item_2 = values_check(False, input_item_2, "side")
        input_item_3 = values_check(False, input_item_3,
            "beverage")
        input_item_4 = values_check(False, input_item_4, "dessert")

        price_1 = values_check(price_1, False, "main course")
        price_2 = values_check(price_2, False, "side")
        price_3 = values_check(price_3, False, "beverage")
        price_4 = values_check(price_4, False, "dessert")

        if input_combo_name in menu.keys():
            while input_combo_name in menu.keys():
                """ Simple loop to check whether the name the user chose for 
                their new combo is already the name of an existing combo on 
                the menu """

                input_combo_name = input_combo_name.title()

                easygui.msgbox(f"{input_combo_name} is already a combo "
                               f"on the menu!", "Invalid Name Chosen")
                print("add combo: invalid - name taken\n")  # print check

                input_combo_name = easygui.enterbox("Enter the combo "
                    "name", "Combo Name")

                input_combo_name = input_combo_name.title()

                if input_combo_name not in menu.keys():
                    print("add combo: valid - name not taken")  # print check
                    input_combo_name = input_combo_name.title()
                else:
                    continue

        total_price = (float(price_1) + float(price_2) + float(price_3) +
            float(price_4))

        print(f"total price is {total_price}")

        new_combo = {
            input_item_1.title(): '$' + price_1,
            input_item_2.title(): '$' + price_2,
            input_item_3.title(): '$' + price_3,
            input_item_4.title(): '$' + price_4,
            "Total Price": f"${total_price:.2f}"
        }

    else:
        values = easygui.multenterbox("Enter combo details",
            "Add Combo", fields)

        if values is None:
            print(type(values))
            print("value is None (if block 1)")
            main_routine()

        if '' in values:
            while '' in values:
                print(type(values))
                easygui.msgbox("Please enter information in all the "
                    "fields or cancel to go back to the start screen.",
                    "Invalid Input(s)")
                values = easygui.multenterbox("Enter combo details",
                    "Add Combo", fields)
                if values is None:
                    print(type(values))
                    print("value is None (last if block)")
                    main_routine()
            print(values)

        (input_combo_name, input_item_1, price_1, input_item_2, price_2,
         input_item_3, price_3) = values

        input_combo_name =  values_check(False, input_combo_name,
            "combo")

        input_item_1 = values_check(False, input_item_1,
            "main course")
        input_item_2 = values_check(False, input_item_2,
            "side")
        input_item_3 = values_check(False, input_item_3,
            "beverage")

        price_1 = values_check(price_1, False, "main course")
        price_2 = values_check(price_2, False, "side")
        price_3 = values_check(price_3, False, "beverage")

        if input_combo_name in menu.keys():
            while input_combo_name in menu.keys():
                """ Simple loop to check whether the name the user chose for 
                their new combo is already the name of an existing combo on
                the menu """

                input_combo_name = input_combo_name.title()

                easygui.msgbox(f"{input_combo_name} is already a combo "
                               f"on the menu!", "Invalid Name Chosen")
                print("add combo: invalid - name taken\n")  # print check

                input_combo_name = easygui.enterbox("Enter the combo "
                    "name", "Combo Name")

                if input_combo_name not in menu.keys():
                    print("add combo: valid - name not taken")  # print check
                    input_combo_name = input_combo_name.title()

        total_price = float(price_1) + float(price_2) + float(price_3)

        price_1 = str(price_1)
        price_2 = str(price_2)
        price_3 = str(price_3)

        new_combo = {
            input_item_1.title(): '$' + price_1,
            input_item_2.title(): '$' + price_2,
            input_item_3.title(): '$' + price_3,
            'Total Price' : f"${total_price:.2f}"
        }

    results = "\n".join([f"  {key}: {value}" for key, value in
        new_combo.items()])

    confirm = easygui.buttonbox("Please take the chance to review the "
        f"following details for your new {input_combo_name.title()} combo\n\n"
        f"{results}", "Details Review",
        choices=["Continue", "Edit", "Remove"])

    menu[input_combo_name] = new_combo
    print(input_combo_name)
    print()
    print(menu)

    if confirm == "Edit":
        edit_combo(input_combo_name)
        result_name = input_combo_name.title() + " Combo"

        results = "\n".join([f"  {key}: {value}" for key, value in
            new_combo.items()])

        easygui.msgbox(result_name + "\n" + results,
            "Combo Successfully Added!")

        main_routine()

    elif confirm == "Remove":
        delete_combo(input_combo_name)

    else:
        result_name = input_combo_name.title() + " Combo"

        easygui.msgbox(result_name + "\n" + results,
                       "Combo Successfully Added!")


def search_combo(combo_name):
    """ Function for searching for an existing combo within the menu """
    while True:
        if combo_name is None:
            main_routine()
        else:
            found = False
            search_term = combo_name.title()
            for combo, combo_items in menu.items():
                if combo == search_term:
                    print("search_combo(): name found")
                    search_results = "\n".join([f"  {key}: {value}" for key,
                    value in combo_items.items()])
                    easygui.msgbox(combo.title() + " Combo" + "\n" +
                    search_results,"Here are your search results")
                    found = True
                    break  # Exit the loop once found
            if not found:
                print("search_combo(): name not found")
                easygui.msgbox(f"Sorry, {combo_name.title()} could not be"
                f" found.","Not Found")

            choice = easygui.buttonbox("Would you like to search again?",
                choices=["Yes", "Cancel"])
            if choice == "Yes":
                combo_name = easygui.enterbox("Please enter the name of "
                    "the combo you would like to search for",
                    "Search for a Combo")
                combo_name = string_check(combo_name)
                search_combo(combo_name)
                main_routine()

            else: main_routine()

def delete_combo(combo_name):
    """ Function which allows the user to delete a combo from the menu """

    if combo_name in menu:
        print(f"\ndelete_combo: {combo_name} is being deleted") # print check
        confirm = easygui.buttonbox("Confirm the deletion of "
            f"the {combo_name.title()} combo?", "Confirm Deletion",
                choices=["Yes", "Cancel"])

        if confirm == "Yes":
            del menu[combo_name]

            full_list = "\n\n".join([combo_name + " Combo\n" + "\n".join([
                f"  {key}: {value}" for key, value in combo_info.items()])
                for combo_name, combo_info in menu.items()])

            easygui.msgbox("Here is the new menu\n\n" + full_list,
                "Updated Menu")

        else:
            main_routine()

    elif menu == {}:
        easygui.msgbox("There is nothing on the menu yet.",
        "Empty Menu")

    else:
        print(f"delete_combo: {combo_name} not on menu")
        choice = easygui.buttonbox(f"{combo_name.title()} is not on the "
            f"menu.", "The combo you want to delete is not on the menu",
            choices=["Cancel", "Enter a new name"])

        if choice == "Enter a new name":
            name = easygui.enterbox("Please enter the name of the "
                "combo you would like to delete","Delete Combo")
            name = string_check(name)
            delete_combo(name)
            main_routine()

def print_menu():
    """ Function which allows the user to show the full menu """
    for key, value in menu.items():
        print(f"  {key}: {value}")

    full_menu = "\n\n".join(
        [f"{combo_name}\n" + "\n".join(
        [f" {key}: {value}" for key, value in combo_info.items()])
         for combo_name, combo_info in menu.items()])

    easygui.msgbox(full_menu, "Full Burger Menu")

    return full_menu

def edit_combo(combo_name):
    """ Function which allows the user to edit details of a combo """

    global old_key
    component_choice = easygui.buttonbox("Please select which part of the "
        "combo you would like to edit", "Component Choice",
        choices=["Name", "Food / Drink", "Price"])

    og_combo = menu[combo_name]
    items = list(og_combo.items())

    if component_choice == "Name":
        while True:
            new_name = easygui.enterbox("Please enter a new name for the "
                f"{combo_name.title()} combo", "Name Choice")
            new_name = string_check(new_name)
            new_name = new_name.title()

            confirm = easygui.buttonbox(f"Confirm changing the"
                f" {combo_name.title()} combo to {new_name.title()}",
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
            choices=["Main Course", "Side", "Beverage", "Dessert"])

        print(items)

        if food_item == "Dessert" and len(items) == 6:
            part_chosen = "dessert"
            print("\nthere is a dessert")
        elif food_item == "Dessert" and len(items) != 6:
            part_chosen = "dessert"
            print("\nthere is no dessert")
            choice = easygui.buttonbox("There is no dessert in the"
                f" {combo_name.title()} Combo. Would you like to remove the "
                f"combo and add a new one?", choices=["Yes", "Cancel"])

            if choice == "Yes":
                delete_combo(combo_name)
                add_combo()
                main_routine()
            else: main_routine()

        elif food_item == "Main Course":
            part_chosen = "main course"
            old_key = items[0][0]
        elif food_item == "Side":
            old_key = items[1][0]
            part_chosen = "side"
        else:
            old_key = items[2][0]
            part_chosen = "beverage"

        og_combo = menu[combo_name]
        list(og_combo.items())

        new_food = easygui.enterbox(f"Please enter a new"
            f" {part_chosen.title()} for the {combo_name.title()} combo",
            f"{part_chosen.title()} - Name Choice")
        new_food = string_check(new_food)
        new_food = new_food.title()

        easygui.msgbox(f"Confirm changing the {part_chosen.title()} for the"
            f" {combo_name.title()} combo from {old_key.title()} to"
            f" {new_food.title()}")

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
        # replaced by the new one

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
                f"Please enter a new price for the {combo_name.title()} "
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
                "would like to search for", "Combo Name")
            name = string_check(name)
            search_combo(name)

        elif choice == "Edit Combo":
            name = easygui.enterbox("Please enter the name of the combo you "
                "would like to edit", "Enter Name")
            name = string_check(name)

            if name.title() not in menu.keys():
                while name.title() not in menu.keys() or None == name:
                    """ Simple loop to check whether the name the user chose for 
                    their new combo is already on the menu """

                    name = name.title()

                    easygui.msgbox(f"{name} is not a combo on the menu!",
                        "Invalid Name Chosen")
                    print("edit combo: invalid - combo entered not on menu\n")
                    # print check

                    name = easygui.enterbox("Enter the combo name",
                        "Combo Name")

                    if name is None:
                        main_routine()
                    
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
        else: quit() # if the user decides to hit 'Exit'

main_routine()