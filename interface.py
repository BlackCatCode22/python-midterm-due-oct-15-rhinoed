# Description: This file contains the menu for the contact manager
# written for python_program_three.py
# modified for python-midterm-program
# File: interface.py
# Author: Mark Edmunds
# Date: 9/12/2023
# modified 10/13/2023


status_message = ""
ver = "0.0.1"
# option for the menu
menu_items = [
    "1 = Process Animals",
    "2 = Output Zoo Population Report",
    "3 = View Hyena Habitat",
    "4 = View Lion Habitat",
    "5 = View Bear Habitat",
    "6 = View Tiger Habitat",
    "7 = exit"
]


# display the menu
def get_menu():
    global ver
    global menu_items
    menu = (
            "**********************************************************************************************\n"
            f"*                        Welcome to Python Zoo Manager {ver}                                 *\n"
            "**********************************************************************************************\n"
            "                       Please select an option from the menu below                            \n"
            " Menu:                                                                                        \n"
            " " + "\n ".join(menu_items) +
            ""
            " "
            " "
    )
    return menu


