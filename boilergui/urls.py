"""boilergui URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dashboard.views import home_view
from dashboard.views import dashboard_view
from dashboard.views import logoutuser
from login.views import login_view
from register.views import register_view
from dashboard.views import changesettings
from boilerconnection.views import updateinfo
from boilerconnection.views import updatesecondaryinfo
from boilerconnection.views import getsecondaryinfo
urlpatterns = [
    path('admin/', admin.site.urls),
	path('', home_view, name='home'),
	path('login/', login_view, name='login'),
	path('register/', register_view, name='register'),
	path('dashboard/', dashboard_view, name='dashboard'),
	path('logout/', logoutuser, name='logout'),
	path('edit/', changesettings, name='edit'),
	path('boilerconnection/',updateinfo, name='boiler'),
	path('ancillary/',updatesecondaryinfo, name='boiler2'),
	path('getancillary/',getsecondaryinfo, name='boiler3')
	
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()