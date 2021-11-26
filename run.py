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


print(SHEET.sheet1.acell('A2'))


def start():
    """
    Gets a user ID to grant access to the program
    repeats code unit a vadil ID is given.
    """
    while True:
        login = input("Please enter your Login ID: ")
        print("-" * 30)

        if validate_id(login):
            print("valid ID, welcome")
            print("-" * 30)
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
        print("To check all stock levels press: 1")
        print("To update all stock levels press: 2")
        print("To update individual stock levels press: 3")
        user_choice = input("Enter: ")

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
        else:
            raise ValueError()
    except ValueError:
        print(f"Invalid choice: {data}")
        print("Please enter 1, 2 or 3.\n")
        return False

    return True


def get_stock_values():
    """
    get stock values and headings to create a dictionary
    """
    headings = SHEET.worksheet("stock").row_values(1)
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    stock_table = {headings[i]: stock_row[i] for i in range(len(stock_row))}

    print("All units are in grams.\n")
    print(stock_table)

    option = input("Would you like to update stocks Y/N: ")
    continue_program(option)


def update_all():
    """
    Get new data for all stock levels
    """
    headings = SHEET.worksheet("stock").row_values(1)
    while True:
        print("Remeber units are in gram's apart from eggs")
        print("And should be separated by commas(1000,200, ...)")
        print(f"Enter new stock blow in the order {headings}")
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
    try:
        [int(num) for num in data]
        if len(data) != 7:
            raise ValueError(
                f"7 values required, you provided {len(data)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_ind():
    """
    function to change individual stock levels.
    """
    headings = SHEET.worksheet("stock").row_values(1)
    print(headings)
    ind_c = input("Please enter the name of the stock to change: ")
    ind_stock = input("And the new stock level: ")

    val_ind_name(ind_c)
    val_ind_stock(ind_stock)


def val_ind_name(name):
    headings = SHEET.worksheet("stock").row_values(1)
    try:
        if name not in headings:
            raise ValueError()
    except ValueError as e:
        print(f"{e}{name} is not in stock worksheet please try again.")
    print("yes")


def val_ind_stock(data):
    """
    Validate if stock is a int.
    """
    try:
        [int(num) for num in data]
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
    print("yes")


def add_new_stock(data):
    """
    Add's new stock data to the worksheet.
    """
    print(f"Updating stock new {data}...")
    stock = SHEET.worksheet("stock")
    stock.append_row(data)


def continue_program(data):
    """
    checkes input is the right value.
    if not raise ValueError>
    if input is correct opens the asked for function.
    """
    try:
        if data == "y":
            update_all()
        elif data == "n":
            exit()
        else:
            raise ValueError()
    except ValueError:
        print(f"Invalid choice: {data}")
        print("Please enter y or n(selection is case sensitive).\n")


def control():
    """
    Main function which starts and controls the program
    """
    print("Welcome to Bakecake stock control terminal")
    print("-" * 30)
    start()
    update_check()


control()
