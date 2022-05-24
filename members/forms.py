from venv import create
import django
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

from lblog.models import Profile

# Creation of Signup forms

class SignUpForm(UserCreationForm):
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model= User
        fields= ('username','first_name','last_name','email','password1','password2')

    def __init__(self, *args,**kwargs):
        super(SignUpForm,self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'
    


# Creation of user update form

class EditProfileForm(UserChangeForm):
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    username= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_login= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    is_superuser= forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_staff= forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_active= forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    date_joined= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model= User
        fields= ('username','first_name','last_name','email','last_login','is_superuser','is_staff','is_active','date_joined','password')

# Password change form

class PasswordChangingForm(PasswordChangeForm):
    old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password1= forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password2= forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))

    class Meta:
        model= User
        fields= ('old_password','new_password1','new_password2')

# Create Profile Form

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('bio','profile_pic','website_url','twitter_url','facebook_url','instagram_url','linkedin_url')
        widgets={
                'bio': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Your Bio'}),
                'website_url': forms.TextInput(attrs={'class':'form-control','id':'elder','value':''}),
                'facebook_url': forms.TextInput(attrs={'class':'form-control','id':'elder','value':''}),
                'twitter_url': forms.TextInput(attrs={'class':'form-control','id':'elder','value':'',}),
                'facebook_url': forms.TextInput(attrs={'class':'form-control','id':'elder','value':'',}),
                'instagram_url': forms.TextInput(attrs={'class':'form-control','id':'elder','value':'',}),
                'linkedin_url': forms.TextInput(attrs={'class':'form-control','id':'elder','value':'',}),
        
    }
