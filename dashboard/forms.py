from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class ProfileForm(forms.Form):
    test_uid=forms.CharField(required=True,label="Test ID",widget=forms.TextInput(attrs={'placeholder': 'Enter Your Test ID'}))
    def clean_renewal_date(self):
       data = self.cleaned_data
       ID=data['test_uid']

       # Check the mobile number. 
       if mobile.isnumeric()==False or len(ID)!=10:
           raise ValidationError(_('Invalid Test ID'))

      

       # Remember to always return the cleaned data.
       return data


