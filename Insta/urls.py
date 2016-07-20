from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/', views.index, name='contact'),
    url(r'^about/how/$', views.faq, name="work"),
    url(r'^about/faq/$', views.faq, name="faq"),
    url(r'^drivers/become/$', views.drivers, name="faq"),
    url(r'^drivers/book/', views.contact, name='contact'),


]