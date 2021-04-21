from django.apps import AppConfig
from core.google_auth import get_google
from stocks.apps import get_sheetsId


class CostConfig(AppConfig):
    name = "cost"


def get_sheet():  # gs 밑에다가
    gc = get_google()
    gs = get_sheetsId()
    result = gc.open_by_key(gs["cost"]).worksheet("kakaoInput")

    return result


def update_cell(when, user, amount, detail, company):
    ws = get_sheet()
    if amount != "":
        values = [when, user, amount, detail, company]
        lastRow = len(ws.col_values(1)) + 1
        for idex, v in enumerate(values):
            ws.update_cell(lastRow, idex + 1, v)
