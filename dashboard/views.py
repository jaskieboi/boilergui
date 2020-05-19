from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout 
from django.db import models
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.forms import ModelForm


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('setsanitaryTemp', 'sethotwaterTemp', 'sanitarystatus','hotwaterstatus')
		
class ProfileForm2(ModelForm):
    class Meta:
        model = Profile
        fields = ('timer1', 'timer2', 'timer3','timer4','timer5','timer6','timer7')
# Create your views here.


def home_view(response,*args,**kwargs):
	return HttpResponse("<h1>Hellod world</h1>")
	
@login_required(login_url='login')
def dashboard_view(request,*args,**kwargs):
    if request.method == 'POST':
        print(request.headers)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        profile_forma = ProfileForm2(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            
            profile_form.save()
          #  messages.success(request, _('Your profile was successfully updated!'))
            return redirect('dashboard')
			
        elif (profile_forma.is_valid()):
            
            profile_forma.save()
          #  messages.success(request, _('Your profile was successfully updated!'))
            return redirect('dashboard')
	
        else:
            messages.error(request, _('Please correct the error below.'))
			
			
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'dashboard.html', {
        'profile_form': profile_form
    })
	
	#return render(response,'dashboard.html')
	
	
	
def logoutuser(request):
	logout(request)
	return redirect('login')
	
	
	
@login_required(login_url='login')
def changesettings(request):
    if request.method == 'POST':
        print(request.headers)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            
            profile_form.save()
          #  messages.success(request, _('Your profile was successfully updated!'))
            return redirect('dashboard')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'edit.html', {
        'profile_form': profile_form
    })
	