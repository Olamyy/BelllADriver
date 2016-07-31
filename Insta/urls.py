from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/', views.index, name='contact'),
    # url(r'^about/how/$', views.faq, name="work"),
    # url(r'^about/faq/$', views.faq, name="faq"),
    # url(r'^drivers/become/$', views.book_driver, name="faq"),
    # url(r'^drivers/book/', views.book_driver, name='contact'),
    # url(r'^drivers/tracker', views.driver_track, name='driver track'),
    # url(r'^track', views.track, name='track'),
    # url(r'^pricing', views.pricing, name='pricing'),
    # url(r'^validate', views.validate, name='validate')


]