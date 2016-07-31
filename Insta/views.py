from django.shortcuts import render
from django.http import HttpResponse
from .forms.book import BookForm
from django.http import HttpResponse
from django.template import RequestContext,Context
from django.core.mail import send_mail


def index(request):
        return render(request, 'Insta/index.html')


# def faq(request):
#     return render(request, 'Insta/faq.html')
#
#
# def drivers(request):
#     if request.method == "POST":
#             return HttpResponse("Got all i need")
#     return render(request, 'Insta/driver.html')
#
#
# def hiw(request):
#     return render(request, 'Insta/hiw.html')
#
#
# def pricing(request):
#     return render(request, 'Insta/pricing.html')
#
#
# def validate(request):
#     return HttpResponse('Got Here')
#
# def book_driver(request):
#     context = RequestContext(request)
#     if request.method == 'POST':
#             user_form = BookForm(data=request.POST)
#             if user_form.is_valid():
#                 user_form.clean()
#                 user_form.save()
#                 return HttpResponse('Details Gotten')
#             else:
#                 print "Invalid"
#                 print user_form.errors
#                 return render(request, 'Insta/driver.html',{'user_form': user_form,
#                                'error_message': user_form.errors}, context)
#     else:
#             user_form = BookForm()
#             print 'Here'
#     return render(request, 'Insta/driver.html', {'form':user_form})
#
#
# def driver_track(request):
#     if request.method == "POST":
#         driver_code = request.POST.get('code')
#
#     return render(request, 'Insta/drivertrack.html')
#
#
# def track(request):
#      session_code = request.POST.get('code')
#
#
#
#
#
#
#
#
#
#
