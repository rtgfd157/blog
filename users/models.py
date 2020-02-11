from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class  Profile(models.Model):
    user = models.OneToOneField(User ,  on_delete=models.CASCADE)
    adress =models.CharField(blank=True,null=True, max_length=100,default="null")
    age = models.IntegerField(null=True,blank=True,default=0)
    Gender = (
        ('-', 'empty'),
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender =models.CharField( max_length=1, choices=Gender,null=True,blank=True,default="-")

    def __str__(self):
        return self.user.username +" Profile"
    
