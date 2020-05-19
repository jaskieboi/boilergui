from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.

from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.forms import ModelForm
from dashboard.models import Profile




class CreateUserForm(UserCreationForm):
	class Meta:
		model=User
		fields=['username','email','password1','password2']
		
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('setsanitaryTemp', 'sethotwaterTemp', 'sanitarystatus','hotwaterstatus')
		
class ProfileForm2(ModelForm):
    class Meta:
        model = Profile
        fields = ('timer1', 'timer2', 'timer3','timer4','timer5','timer6','timer7','batterystatus','batterylevel','heaters')
		
		
		
@csrf_exempt 		

def updateinfo(request,*args,**kwargs):
	if request.method == 'POST':
		
		user= authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
		
		if user is not None:
			login(request, user)
			profile_form = ProfileForm(request.POST, instance=request.user.profile)
			if profile_form.is_valid():
				profile_form.save()
			print (request.POST)
			#logout(request)
			return render(request,'displaydata.html')
		else : 
			messages.info(request,'username or password incorrect')
			
	#logout(request)
	return render(request,'displaydata.html')
	
	
	
@csrf_exempt 		

def updatesecondaryinfo(request,*args,**kwargs):
	if request.method == 'POST':
		
		user= authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
		
		if user is not None:
			login(request, user)
			profile_form2 = ProfileForm2(request.POST, instance=request.user.profile)
			if profile_form2.is_valid():
				profile_form2.save()
			print (request.POST)
			#logout(request)
			return render(request,'anciliary.html')
		else : 
			messages.info(request,'username or password incorrect')
			
	#logout(request)
	return render(request,'anciliary.html')
	
	
	
@csrf_exempt 
def getsecondaryinfo(request,*args,**kwargs):
	if request.method == 'POST':
		
		user= authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
		
		if user is not None:
			login(request, user)
			return render(request,'anciliary.html')
		else : 
			messages.info(request,'username or password incorrect')
			
	#logout(request)
	return render(request,'anciliary.html')
			

	