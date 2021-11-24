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
    login = input("Please enter your Login ID: ")
    print("-" * 30)
    validate_id(login)


def validate_id(data):
    """
    Checkes to see if the given id is correct.
    Checkes to see if all values are integers
    and that they are the correct ones if not
    raises a ValueError.
    """
    id = "1234"
    
    try:
        if id != data:
            raise ValueError()
    except ValueError as e:
        print(f"Incorrect ID: {data}, Please try again.")


print("Welcome to Bakecake stock control terminal")
print("-" * 30)
start()
