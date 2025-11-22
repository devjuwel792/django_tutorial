from django.http import HttpResponse
from django.shortcuts import render


def aboutUs(request):
    return render(request, "about.html")


def service(request):
    return render(request, "service.html")


def contact(request):
    return render(request, "contact.html")


def course(request):
    return HttpResponse("Welcome to about page .")


def courseDetail(request, id):
    return HttpResponse(id)


def homePage(request):
    return render(request, "index.html")
