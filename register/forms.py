from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class RegisterForm(forms.Form):
    student_name=forms.CharField(required=True,label="Student's Name",widget=forms.TextInput(attrs={'placeholder': 'Enter Your Full Name'}))
    student_mobile=forms.CharField(required=True,label="Student's Mobile Number",widget=forms.TextInput(attrs={'placeholder': 'Enter Your Mobile Number'}))
    student_email=forms.EmailField(required=True,label="Student's Email",widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email ID'}))
    student_password=forms.CharField(required=True,label="Student's Password",widget=forms.PasswordInput)
    student_confirm_password=forms.CharField(required=True,label="Confirm Password",widget=forms.PasswordInput)

    def clean_renewal_date(self):
       data = self.cleaned_data
       mobile=data['student_mobile']
       pwd=data['student_password']
       cnfm_pwd=data['student_confirm_password']

       # Check the mobile number. 
       if mobile.isnumeric()==False or len(mobile)!=10:
           raise ValidationError(_('Invalid Mobile Number not a 10 digit number'))

       # Check if a date is in the allowed range (+4 weeks from today).
       if pwd!=cnfm_pwd:
           raise ValidationError(_('Passwords donot match'))

       # Remember to always return the cleaned data.
       return data

class LoginForm(forms.Form):
    student_email=forms.EmailField(required=True,label="Student's Email",widget=forms.EmailInput(attrs={'placeholder': 'Registered Email ID'}))
    student_password=forms.CharField(required=True,label="Student's Password",widget=forms.PasswordInput)
    
    def clean_renewal_date(self):
       data = self.cleaned_data
       return data

