from django import forms
from .models import *
from django.core.validators import RegexValidator


class OrderForm(forms.Form):
    adress = forms.CharField(label='Адрес доставки')
    tel = forms.CharField(label='Телефон', validators=[RegexValidator('^\\+7-\\d{3}-\\d{3}-\\d{2}-\\d{2}$', message='введите правильный телефон +7***-***-**-**')])
    email = forms.EmailField(label='Email')
