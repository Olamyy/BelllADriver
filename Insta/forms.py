from django import forms
from Insta.models import Contact, Driver, Plan


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'






