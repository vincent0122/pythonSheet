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


def update_cell():
    ws = get_sheet()
    ws.update("a1000", "hahaha")
