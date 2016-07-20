from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail


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
            print "Got Method"
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            email = request.POST.get('email')
            number = request.POST.get('number')
            address = request.POST.get('address')
            sex = request.POST.get('sex')
            payment = request.POST.get('payment')
            plan = request.POST.get('plan')
            print firstname,lastname, email,number,address,sex, payment, plan
            try:
                    send_mail(
                        subject='New InstaDriva Request',
                        message='''A new driver request has been made. The request details are below:'
                                'firstname : {0},',
                                'lastname: {1},'
                                'email : {2},'
                                'mobile_number : {3},'
                                'address : {4},'
                                 'sex : {5},'
                                'payment : {6}'
                                 'plan :{7}'''.format(firstname, lastname,email, number, address, sex , payment, plan),
                                from_email='olamyy53@gmail.com',
                                recipient_list=['lutherlawoyin@gmail.com']
                    )
                    return render(request, 'Insta/success.html')
            except:
                return  HttpResponse('An error occured')

    return render(request, 'Insta/book.html')










