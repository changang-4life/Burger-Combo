"""Program which stores a quick menu of the combo meals for a friend's
takeaway business
Jade Akinbo
v1 - main_routine() and menu Details
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

"""Main Routine"""
choice = easygui.buttonbox("Please choose an action", "Menu Options",
    choices = ["Exit"])

if choice == "Exit":
    quit()