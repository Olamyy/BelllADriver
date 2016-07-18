import json
from django.shortcuts import render
from .forms import ContactForm, DriverForm, PlanForm
from django.http import HttpResponse


def index(request):
        return render(request, 'Insta/index.html')


def faq(request):
    return render(request, 'Insta/faq.html')


def drivers(request):
    if request.method == "POST":
        print "Am in driver form"
        driverform = DriverForm(request.POST)
        if driverform.is_valid():
            return HttpResponse("Got all i need")
        elif driverform.errors:
            print "Driver Form is not valid"
            return render(request, 'Insta/driver.html',
                          {'contact': driverform})
    else:
        print "First view"
        driverform = DriverForm()
        return render(request, 'Insta/driver.html',
                      {'driverform': driverform})


def contact(request):
    if request.method == "POST":
        print  "Am in contact form"
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            print "Contact Form is valid"
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            number = request.POST.get('number')
            email = request.POST.get('email')
            pickup = request.POST.get('pickup_address')
            plan = request.POST.get('plan')
            sex = request.POST.get('driver_sex')
            pay = request.POST.get('payment')
            return HttpResponse(json.dumps({'message': (first_name, last_name, number, email, pickup, plan, sex, pay)}))
        elif contactform.errors:
            print "Contact Form is not valid"
            return render(request, 'Insta/index.html',
                          {'contact': contactform})
    else:
        print "First view"
        contactform = ContactForm()
        plan = PlanForm()
        return render(request, 'Insta/book.html',
                  {'contact': contactform,'plan': plan})


def contact_success(request):
    return HttpResponse("Thank you")









