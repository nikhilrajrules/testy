from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class TestForm(forms.Form):

    ans1 = forms.BooleanField(required=False,label='')
    ans2 = forms.BooleanField(required=False,label='')
    ans3 = forms.BooleanField(required=False,label='')
    ans4 = forms.BooleanField(required=False,label='')
    
    def clean_renewal_date(self):
       data = self.cleaned_data
       one=data['ans1']
       two=data['ans2']
       three=data['ans3']
       four=data['ans4']
       if one==False and two==False and Three==False and four==False:
       	   raise ValidationError(_('Plese select any Option'))


      

       # Remember to always return the cleaned data.
       return data


