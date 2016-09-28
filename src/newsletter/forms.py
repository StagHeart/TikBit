from django import forms
from django.core.validators import RegexValidator
from .models import *

# All forms go here.

# --Contact Forms--

# --General Contact Form--
class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = forms.CharField(validators=[phone_regex], required=False) # validators should be a list

# --Business Contact Form--
class BusinessContactForm(forms.Form):
    full_name = forms.CharField(required=True)
    business_name = forms.CharField(required=False)
    email = forms.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = forms.CharField(validators=[phone_regex], required=False) # validators should be a list
    
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))    

# --Terminal Forms
class viewZeroForm(forms.Form):
    zero = forms.BooleanField(required=True,initial=True,label='Zero Views')
    
# All Sign Up
class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']
        ### exclude = ['full_name']

    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        return full_name

# --GAMES--

# Squiggles Sign Up Form
class SignUpFormSquiggles(forms.ModelForm):
    class Meta:
        model = SignUp_Squiggles
        fields = ['full_name', 'email']
        ### exclude = ['full_name']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')
        
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        
        return full_name

class SignUpFormRanger(forms.ModelForm):
    class Meta:
        model = SignUp_Ranger
        fields = ['full_name', 'email']
        
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')
        
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        
        return full_name

# --APPS--
# Good News Sign Up Form
class SignUpFormGoodNews(forms.ModelForm):
    class Meta:
        model = SignUp_GoodNews
        fields = ['full_name', 'email']
        
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')
        
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        
        return full_name

# Herbs Sign Up Form
class SignUpFormHerbs(forms.ModelForm):
    class Meta:
        model = SignUp_Herbs
        fields = ['full_name', 'email']
        
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')
        
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        
        return full_name

# Friends Sign Up Form
class SignUpFormFriends(forms.ModelForm):
    class Meta:
        model = SignUp_Friends
        fields = ['full_name', 'email']
        ### exclude = ['full_name']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')
        
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        
        return full_name

# Fitness Sign Up Form
class SignUpFormFitness(forms.ModelForm):
    class Meta:
        model = SignUp_Fitness
        fields = ['full_name', 'email']
        
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        
        return full_name

