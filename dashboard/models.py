from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	setsanitaryTemp = models.CharField(max_length=2, default='1',null=True)
	sethotwaterTemp = models.CharField(max_length=2, default='2',null=True)
	actualsanitaryTemp = models.CharField(max_length=2, default='3',null=True)
	actualhotwaterTemp = models.CharField(max_length=2, default='4',null=True)
	timer1 = models.CharField(max_length=200, default='6',null=True)
	timer2 = models.CharField(max_length=200, default='6',null=True)
	timer3 = models.CharField(max_length=200, default='6',null=True)
	timer4 = models.CharField(max_length=200, default='6',null=True)
	timer5 = models.CharField(max_length=200, default='6',null=True)
	timer6 = models.CharField(max_length=200, default='6',null=True)
	timer7 = models.CharField(max_length=200, default='6',null=True)
	sanitarystatus = models.CharField(max_length=200, default="t",null=True)
	hotwaterstatus = models.CharField(max_length=200, default="t",null=True)
	batterystatus= models.CharField(max_length=200, default='8',null=True)
	batterylevel = models.CharField(max_length=200, default='9',null=True)
	heaters = models.CharField(max_length=200, default='10',null=True)
	
	def __str__(self):
		return str({self.user.username})
# Create your models here.
