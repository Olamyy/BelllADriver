import json
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
        return render(request, 'Insta/index.html')


def faq(request):
    return render(request, 'Insta/faq.html')


def drivers(request):
    if request.method == "POST":
            return HttpResponse("Got all i need")

    return render(request, 'Insta/driver.html')


def contact(request):
    if request.method == "POST":
            author = request.POST.get('author')
            email = request.POST.get('email')
            number = request.POST.get('number')
            address = request.POST.get('address')
            sex = request.POST.get('sex')
            payment = request.POST.get('payment')
            plan = request.POST.get('plan')
            return HttpResponse(json.dumps({'message': (author, email, number, address, plan, payment)}))

    return render(request, 'Insta/book.html')


def contact_success(request):
    return HttpResponse("Thank you")









