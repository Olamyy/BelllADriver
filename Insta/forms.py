from django import forms
from Insta.models import Contact, Driver, Plan


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        # labels = ''
        widgets = {
            'name':forms.TextInput(
                attrs={'id':'first_name','class':'form-control', 'required':True, 'placeholder':'First name', 'label':''}
            ),
            'number':forms.NumberInput(
                attrs={'id':'number', 'required':True, 'placeholder':'Mobile number', 'label':''}
            ),
            'email':forms.EmailInput(
                attrs={'id':'email', 'required':True, 'placeholder':'Email', 'label':''}
            ),
            'pickup_address':forms.EmailInput(
                attrs={'id':'address', 'required':True, 'placeholder':'Address', 'label':''}
            )

        }


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={'id': 'first_name', 'required': True, 'placeholder': 'First name', 'label': ''}
            ),
            'last_name': forms.TextInput(
                attrs={'id': 'last_name', 'required': True, 'placeholder': 'Last name', 'label': ''}
            ),
            'number': forms.NumberInput(
                attrs={'id': 'number', 'required': True, 'placeholder': 'Mobile number', 'label': ''}
            ),
            'email': forms.EmailInput(
                attrs={'id': 'email', 'required': True, 'placeholder': 'Email', 'label': ''}
            ),
            'home_address': forms.EmailInput(
                attrs={'id': 'address', 'required': True, 'placeholder': 'Address', 'label': ''}
            ),
            'residence_years': forms.TextInput(
                attrs={'id': 'first_name', 'required': True, 'placeholder': 'First name', 'label': ''}
            ),
            'lasdri': forms.TextInput(
                attrs={'id': 'last_name', 'required': True, 'placeholder': 'Last name', 'label': ''}
            ),
            'driver_sex': forms.MultipleChoiceField(),
            'experience_years': forms.NumberInput(
                attrs={'id': 'experience', 'required': True, 'placeholder': 'Experience years', 'label': ''}
            )

        }






