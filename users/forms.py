from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()


    class Meta:
        model=User
        fields=['username','email','password1','password2']



class UserUpdateForm(forms.ModelForm):
         email = forms.EmailField()
         


         class Meta:
             model =User
             fields=['username','email']

class ProfileUpdateForm(forms.ModelForm):
    adress = forms.CharField(label='Adress', max_length=100)
    age = forms.IntegerField(label='Age')
    Gender = (
          ('-', 'empty'),
          ('M', 'Male'),
          ('F', 'Female'),
               )

    gender=forms.Select(  choices=Gender)

    class Meta:
        model =Profile
        fields=['adress','age','gender']