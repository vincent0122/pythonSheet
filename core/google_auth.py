import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials
from config.settings import SERVER


def get_google():

    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]

    if SERVER == "l":
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            "./creden/google-credentials.json", scope
        )
    elif SERVER == "s":
        json = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
        credentials = ServiceAccountCredentials.from_json_keyfile_name(json, scope)

    gc = gspread.authorize(credentials)
    return gc
