from django import forms
from Insta.models import Contact


class BookForm(forms.ModelForm):
   class Meta:
       model = Contact
       fields = ['first_name', 'last_name', 'email', 'driver_sex', 'number', 'payment', 'pickup_address', 'plan']
