from django import forms

class Nameform(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    year = forms.CharField(label='Kaori year', max_length=100)

