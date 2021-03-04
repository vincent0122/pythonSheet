# Create class name and init function
import gspread
import pandas as pd
from gspread_dataframe import get_as_dataframe
from oauth2client.service_account import ServiceAccountCredentials


class GoogleSheetProcessor:
    def __init__(self):
        self.scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive",
        ]
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(
            "./env/Credentials.json", self.scope
        )
        self.gc = gspread.authorize(self.credentials)

    # Get google sheet method
    def obtain_google_sheet(self, link):
        sheet = self.gc.open_by_url(link)
        sheet = sheet.get_worksheet(0)
        return sheet

    # Convert sheet to data frame and drop unnecessary rows and columns
    @staticmethod
    def worksheet_to_df(worksheet):
        # adjust input so nan rows and columns are not imported
        df = get_as_dataframe(worksheet, parse_dates=True, header=0)
        df.dropna(axis="columns", how="all", inplace=True)
        df.dropna(axis="rows", how="all", inplace=True)
        return df