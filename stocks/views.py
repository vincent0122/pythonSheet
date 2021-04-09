from django.shortcuts import render
from .apps import (
    cleaning_datas,
    making_graph,
    date_setting,
    basic_setting,
    get_current_stock,
)

items = basic_setting["items"]


def get_html(request):
    date_range = {
        "start": request.GET.get("start"),
        "last": request.GET.get("last"),
        "wv": request.GET.get("wv"),
    }

    return date_range


def stock_future(request):
    date_data = date_setting()
    last = date_data["yesterday"]
    start = date_data["history_start"]
    wv = 1

    date_range = get_html(request)
    if date_range["start"] is not None:
        start = date_range["start"]
        last = date_range["last"]
        wv = int(date_range["wv"]) / 100

    values_df = cleaning_datas()
    fig = making_graph(values_df, start, last, wv)
    graph = fig.to_html(full_html=False)
    wvh = wv * 100

    return render(
        request,
        "stocks/stock_future.html",
        {"graph": graph, "last": last, "start": start, "wvh": wvh},
    )


def stock_item(request):
    item = request.GET.get("product")
    current_stock = get_current_stock()
    value = current_stock["제품명"] == item
    value2 = current_stock[value]
    print(value2.수량)

    return render(request, "stocks/stock_item.html", {"items": items})
