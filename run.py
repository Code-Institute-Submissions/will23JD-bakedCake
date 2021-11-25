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
    code = "1234"

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
        print("Would you like to update or check on stock levels?")
        user_choice = input("Enter C to check OR U to update: ")

        if validate_c(user_choice):
            break


def validate_c(data):
    """
    checks whether the user wants to update stock levels
    or check them.
    """

    try:
        if data == "U":
            get_new_stock()
        elif data == "C":
            get_stock_values()
        else:
            raise ValueError()
    except ValueError:
        print(f"Invalid choice: {data}")
        print("Please enter C or U(selection is case sensitive).\n")
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


def get_new_stock():
    """
    Lets the user chose wether they want to update all stocks
    or individual stocks.
    """

    print("Would you like to up date all stocks or individual stocks?")
    choice = input("Enter: A for all Or: I for individual:")

    validate_new_stock(choice)


def validate_new_stock(data):
    """
    checks whether the user wants to update stock levels
    or check them.
    """
    try:
        if data == "A":
            print("update_all()")
        elif data == "I":
            print("update_individual()")
        else:
            raise ValueError()
    except ValueError:
        print(f"Invalid choice: {data}")
        print("Please enter A or I(selection is case sensitive).\n")


def control():
    print("Welcome to Bakecake stock control terminal")
    print("-" * 30)
    start()
    update_check()


control()
