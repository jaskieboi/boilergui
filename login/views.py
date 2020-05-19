from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.

from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt



class CreateUserForm(UserCreationForm):
	class Meta:
		model=User
		fields=['username','email','password1','password2']
		
		
		
@csrf_exempt 		
def login_view(request,*args,**kwargs):
	if request.user.is_authenticated:
		return redirect('dashboard')
	else:
		if request.method == 'POST':
		
			user= authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
			if user is not None:
				login(request, user)
				print(request.POST)
				return redirect('dashboard')
				#return render(request,'displaydata.html')
			else : 
				messages.info(request,'username or password incorrect')
			
		context={}
		return render(request,'login.html', context)
	
