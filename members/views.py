from dataclasses import field
from lblog.models import Profile
from pyexpat import model
from re import template
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic import DetailView,CreateView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from members.forms import EditProfileForm, PasswordChangingForm, ProfilePageForm, SignUpForm


# Creation of User registration view

class UserRegisterView(generic.CreateView):
    form_class=SignUpForm
    template_name='registration/register.html'
    success_url=reverse_lazy('login')


# Creation of User edit profile view

class UserEditView(generic.UpdateView):
    form_class=EditProfileForm
    template_name='registration/edit_profile.html'
    success_url=reverse_lazy('home')

    def get_object(self):
        return self.request.user

# Password Change View

class PasswordsChangeView(PasswordChangeView):
    form_class=PasswordChangingForm
    success_url=reverse_lazy('password_success')

# Password change success views

def password_success(request):
    return render(request,'registration/password_success.html',{})

# creation of profile view

class ShowProfilePageView(DetailView):
    model=Profile
    template_name='registration/user_profile.html'

    def get_context_data(self,*args, **kwargs):
        context=super(ShowProfilePageView,self).get_context_data(*args,**kwargs)

        page_user =get_object_or_404(Profile,id=self.kwargs['pk'])
        context["page_user"]=page_user
        return context
# Edit profile view

class EditProfilePageView(generic.UpdateView):
    model=Profile
    template_name='registration/edit_profile_page.html'
    fields=['bio','profile_pic','website_url','twitter_url','facebook_url','instagram_url','linkedin_url']
    success_url=reverse_lazy('home')

# create user profile page
class CreateProfilePageView(CreateView):
    model=Profile
    form_class=ProfilePageForm
    template_name='registration/Create_user_profile.html'

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)

    