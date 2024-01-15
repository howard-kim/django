# from django.http import HttpResponse

# def main(request):
#     return HttpResponse("Hello, this is Pyburger")

# def burger_list(request):
#     return HttpResponse("This is the list of Burgers in Pyburger")

from django.shortcuts import render
from burgers.models import Burger


def main(request):
    return render(request, "main.html")

def burger_list(request):
    burgers = Burger.objects.all()
    # print("전체 햄버거 목록:", burgers)

    ctx = {
        "burgers": burgers,
    }
    return render(request, "burger_list.html", ctx)

def burger_search(request):
    keyword = request.GET.get("keyword")

    if keyword is not None:
        burgers = Burger.objects.filter(name__contains=keyword)
    else:
        burgers = Burger.objects.none()
    # print(keyword)
    # print(request.GET)
    ctx = {
        "burgers": burgers,
    }

    print(burgers)
    return render(request, "burger_search.html", ctx)