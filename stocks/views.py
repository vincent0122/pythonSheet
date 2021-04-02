from django.shortcuts import render
from .apps import cleaning_datas, making_graph, date_setting


def get_html(request):
    date_range = {"start": request.GET.get("start"), "last": request.GET.get("last")}

    return date_range


def stock_future(request):
    date_data = date_setting()
    last = date_data["yesterday"]
    start = date_data["history_start"]

    if get_html(request) is not None:
        date_range = get_html(request)
        start = date_range["start"]
        last = date_range["last"]
        print(start)

    values_df = cleaning_datas()
    fig = making_graph(values_df, 1)
    graph = fig.to_html(full_html=False)
    return render(
        request,
        "stocks/stock_future.html",
        {"graph": graph, "last": last, "start": start},
    )


# def stock_future(request):
#     return render(
#         request,
#         "stocks/stock_future.html",
#     )
