from google_home import GoogleSheetProcessor

gp = GoogleSheetProcessor()
data = gp.obtain_google_sheet(
    "https://docs.google.com/spreadsheets/d/1U4pgA9tfj2sciXj_6LMQ74Vff81OButlpOBb_RVvH9c/edit#gid=1327491373"
)
data = gp.worksheet_to_df(data)
print(data)