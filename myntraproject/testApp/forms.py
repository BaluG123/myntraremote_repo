from django import forms
from django.contrib.auth.models import User
from testApp.models import buyer

class signupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']

class infoform(forms.Form):
    name=forms.CharField()
    gender=forms.CharField()
    phno=forms.IntegerField()
    email=forms.EmailField()

class buyerForm(forms.ModelForm):
    class Meta:
        model=buyer
        fields='__all__'
