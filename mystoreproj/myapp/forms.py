from django import forms
import datetime


class UserForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    address = forms.CharField(max_length=100)


class ImageForm(forms.Form):
    image = forms.ImageField()


class ProductForm(forms.Form):
    prod_name = forms.CharField(max_length=100)
    description = forms.CharField()
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    prod_count = forms.IntegerField()
    add_date = forms.DateTimeField(initial=datetime.date.today)
    #image = forms.ImageField()
