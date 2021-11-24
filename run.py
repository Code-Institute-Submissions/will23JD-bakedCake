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
    except ValueError as e:
        print(f"{e}Incorrect ID: {data}, Please try again.")
        print("x" * 30)
        return False

    return True


def update_check():
    """
    Asks the user if they want to check on stock levels
    or update them.
    """
    print("Would you like to update or check on stock levels?")
    user_choice = input("Enter C to check OR U to update: ")

    validate_c_u(user_choice)


def validate_c_u(data):
    """
    checks whether the user wants to update stock levels
    or check them.
    """
    update = "U"
    check = "C"

    try:
        if data == update:
            print("update()")
        elif data == check:
            print("check()")
        else:
            raise ValueError()
    except ValueError as e:
        print(f"{e}Invalid choice: {data}, selection is case sensitive.")


print("Welcome to Bakecake stock control terminal")
print("-" * 30)
start()
update_check()
