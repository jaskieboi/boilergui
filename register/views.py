from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import *
from dashboard.models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver

class CreateUserForm(UserCreationForm):
	class Meta:
		model=User
		fields=['username','email','password1','password2']
		
@csrf_exempt 		
def register_view(request,*args,**kwargs):
	if request.user.is_authenticated:
		return redirect('dashboard')
	else:
		form = CreateUserForm()
	
		if request.method=='POST':
			form=CreateUserForm(request.POST)
			if form.is_valid():
				print(request.POST)
				form.save()
				user=form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)
				return redirect('login')
				
		context={'form':form}
		return render(request,'registration.html', context)
		
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
