import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials


def get_google():
    json = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    # credentials = ServiceAccountCredentials.from_json_keyfile_name(
    #     "./creden/google-credentials.json", scope
    # )  # Your json file here
    credentials = ServiceAccountCredentials.from_json_keyfile_name(json, scope)
    gc = gspread.authorize(credentials)
    return gc
