<<<<<<< HEAD
from django import forms
from .models import PersonData


class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'يرجى ادخال الاسم هنا',
        'type': 'text'
    }))
    phone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'يرجى ادخال رقم الهاتف',
        'type': 'text'
    }))
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control ',
        'placeholder': 'يرجى ادخال العنوان',
        'type': 'text'
    }))
    data = forms.CharField(max_length=2000, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'يرجى ادخال الطلب او الشكوى',
        'type': 'textarea'
    }))
=======
from django import forms
from .models import PersonData


class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'يرجى ادخال الاسم هنا',
        'type': 'text'
    }))
    phone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'يرجى ادخال رقم الهاتف',
        'type': 'text'
    }))
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control ',
        'placeholder': 'يرجى ادخال العنوان',
        'type': 'text'
    }))
    data = forms.CharField(max_length=2000, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'يرجى ادخال الطلب او الشكوى',
        'type': 'textarea'
    }))
>>>>>>> bb806d06e1365e7e16a45a26f04abc01c041c109
