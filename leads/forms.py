from django import forms
from .views import *
from django.contrib.auth.forms import UserCreationForm ,  UsernameField
from  .models  import Lead
from django.contrib.auth import get_user_model

User = get_user_model()



class CustomerCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}


class LeadModelForms(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'


class LeadFrom(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)
