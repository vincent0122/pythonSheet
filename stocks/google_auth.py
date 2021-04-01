import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

SECRET_KEY = os.getenv("SECRET_KEY")


def get_google():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        os.getenv(), scope
    )  # Your json file here
    gc = gspread.authorize(credentials)
    return gc
