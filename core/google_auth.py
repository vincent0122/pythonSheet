import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials
from config.settings import DEBUG


def get_google():

    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]

    if DEBUG:
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            "./creden/google-credentials.json", scope
        )
    else:
        json = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
        credentials = ServiceAccountCredentials.from_json_keyfile_name(json, scope)

    gc = gspread.authorize(credentials)
    return gc
