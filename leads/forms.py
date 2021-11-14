from django import forms
from .views import *


class LeadModelForms(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'


class LeadFrom(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)
