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
    

print("Welcome to Bakecake stock control terminal")
print("-" * 30)
start()
