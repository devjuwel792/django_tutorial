from django.http import HttpResponse
from django.shortcuts import render


def aboutUs(request):

    return HttpResponse("Welcome to about page .")


def course(request):
    return HttpResponse("Welcome to about page .")


def courseDetail(request, id):
    return HttpResponse(id)


def homePage(request):
    data = {
        "title": "Home new",
        "subtitle": "Bangladesh is a small country",
        "skills": [10, 20, 30, 40.55, 55, 67, 76, 34, 32, 23],
        "student_details": [{"name": "Juwel Rana", "id": "4225020"}],
    }
    return render(request, "index.html", data)
