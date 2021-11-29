import os
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Bakedcake')

HEADINGS = SHEET.worksheet("stock").col_values(1)


def start():
    """
    Gets a user ID to grant access to the program
    repeats code unit a vadil ID is given.
    """
    while True:
        login = input("Please enter your Login ID: ")
        spacer(35)

        if validate_id(login):
            print("valid ID, welcome")
            spacer(35)
            break


def validate_id(data):
    """
    Checkes to see if the given id is correct.
    Checkes to see if all values are integers
    and that they are the correct ones if not
    raises a ValueError.
    """
    code = "1"

    try:
        if code != data:
            raise ValueError()
    except ValueError:
        print(f"Incorrect ID: {data}, Please try again.")
        print("x" * 30)
        return False

    return True


def update_check():
    """
    Asks the user if they want to check on stock levels
    or update them.
    """
    while True:
        print("To check all stock levels enter: 1")
        print("To update all stock levels enter: 2")
        print("To update individual stock levels enter: 3")
        print("To add a new item enter: 4")
        print("To delete a item enter: 5")
        user_choice = input("Enter: ")
        spacer(35)

        if validate_c(user_choice):
            break


def validate_c(data):
    """
    checks whether the user wants to update stock levels
    or check them.
    """

    try:
        if data == "1":
            get_stock_values()
        elif data == "2":
            update_all()
        elif data == "3":
            update_ind()
        elif data == "4":
            add_items()
        elif data == "5":
            get_del_item()
        else:
            raise ValueError()
    except ValueError:
        print(f"Invalid choice: {data}")
        print("Please enter 1, 2, 3, 4 or 5.\n")
        return False

    return True


def get_stock_values():
    """
    get stock values and headings to create a dictionary
    """
    clear_console()
    stock = SHEET.worksheet("stock").col_values(2)
    stock_table = {HEADINGS[i]: stock[i] for i in range(len(HEADINGS))}
    print("STOCK TABLE")
    spacer(35)
    print("All units are in grams.\n")
    for key, value in stock_table.items():
        print(f"{key} : {value}")

    option = input("\nWould you like to continue(c) or logout(l): ")
    spacer(35)
    continue_program(option)


def update_all():
    """
    Get new data for all stock levels
    """
    clear_console()
    print("UPDATE ALL STOCK")
    spacer(35)
    while True:
        print("Remeber units are in gram's apart from eggs")
        print("And should be separated by commas(1000,200, ...)")
        print(f"Enter new stock blow in the order {HEADINGS}\n")
        all_stock = input("New stock: ")

        new_stock = all_stock.split(",")

        if validate_stock(new_stock):
            print("Correct input")
            break

    add_new_stock(new_stock)


def validate_stock(data):
    """
    The try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't 7 values.
    """
    index = []
    for i in range(len(HEADINGS)):
        index.append(i)
    try:
        [int(num) for num in data]
        if len(data) != len(index):
            raise ValueError(
                f"{len(index)} values required, you provided {len(data)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_ind():
    """
    function to change individual stock levels.
    """
    clear_console()
    print("UPDATE INDIVIDUAL STOCK")
    spacer(35)
    while True:
        names = {HEADINGS[i]: i + 1 for i in range(len(HEADINGS))}
        for key, value in names.items():
            print(f"{key} : {value}")
        ind_c = input("\nPlease enter the number of the stock to change: ")
        ind_stock = input("And the new stock level: ")

        if val_ind_name(ind_c) and val_ind_stock(ind_stock):
            break
    print("\nAdding new stock...")
    update_stock(ind_c, ind_stock)
    print("New stock added.")
    option = input("\nWould you like to continue(c) or logout(l): ")
    spacer(35)
    continue_program(option)


def val_ind_name(name):
    """
    Function to check is input stock is on the worksheet.
    If not returns false causing the while loop to continue.
    """
    index = []
    for i in range(len(HEADINGS)):
        index.append(i + 1)
    try:
        if int(name) not in index:
            raise ValueError()
    except ValueError as e:
        print(f"{e}{name} is not in stock worksheet please try again.")
        return False

    return True


def val_ind_stock(data):
    """
    Validate if stock is a int.
    If not returns false causing the while loop to continue.
    """
    try:
        [int(num) for num in data]
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def add_new_stock(data):
    """
    Add's new stock data to the worksheet.
    """
    print(f"Adding stock new {data}...")
    all_stock = {data[i]: i + 1 for i in range(len(data))}

    for stock, name in all_stock.items():
        update_stock(name, stock)
    print("New stock added.")
    option = input("\nWould you like to continue(c) or logout(l): ")
    spacer(35)
    continue_program(option)


def update_stock(name, data):
    """
    Add new stock name and stock level to google sheet.
    """
    SHEET.sheet1.update_cell(name, 2, data)


def add_items():
    """
    Get new stock new and stock level.
    pass them to validation function.
    """
    clear_console()
    print("ADD NEW ITEM")
    spacer(35)
    while True:
        print("Please enter the name of the item you wish to add:")
        name = input("Enter: ")
        print("\nPlease enter the quantity of the item(in grams)")
        stock = input("Enter: ")

        if val_ind_stock(stock):
            break
    print(f"\nAdding new item: {name} and value: {stock}...")
    append_n_stock(name, stock)
    print(f"New item: {name} and value: {stock} Added.")
    spacer(35)
    exit()


def append_n_stock(name, data):
    """
    Append new stock new and data.
    """
    for i in range(len(HEADINGS)):
        new = i + 2
    SHEET.sheet1.update_cell(new, 1, name)
    SHEET.sheet1.update_cell(new, 2, data)


def get_del_item():
    """
    Get user choice for item to delete from google sheets.
    Pass choice to validation to check its an int.
    """
    clear_console()
    print("DELETE ITEM")
    spacer(35)
    while True:
        print("Please enter the number of the item you would like to delete.")
        names = {HEADINGS[i]: i + 1 for i in range(len(HEADINGS))}
        for key, value in names.items():
            print(key, ':', value)
        remove = input("\nEnter: ")

        if val_ind_name(remove):
            break
    print("\nRemoving item....")
    delete_item(remove)
    print("Item deleted.")
    spacer(35)
    exit()


def delete_item(row):
    """
    get row from user input and delete from google sheet.
    """
    SHEET.sheet1.delete_rows(int(row))


def continue_program(data):
    """
    Get's use input if they want to continue or logout.
    Validates respons with try statement.
    """
    try:
        if data == "c":
            update_check()
        elif data == "l":
            control()
        else:
            raise ValueError()
    except ValueError:
        print(f"Invalid choice: {data}")
        print("Please enter c or l(selection is case sensitive).\n")


def clear_console():
    """
    Clears the terminal to stop it getting cluttered
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def spacer(num):
    """
    creates a ---- string to space out text.
    """
    print("-" * num)


def control():
    """
    Main function which starts and controls the program
    """
    clear_console()
    print("Welcome to Bakecake stock control terminal")
    spacer(35)
    start()
    clear_console()
    update_check()


control()
