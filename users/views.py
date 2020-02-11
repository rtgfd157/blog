from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from .models import User
from .forms import ProfileUpdateForm
from .forms import UserUpdateForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            string='Acount created for please Log In : '+ username+'!'
            messages.success(request,string )
            return redirect('blog-home')

            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)

    else:
        form = UserRegisterForm()

    return render (request,'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form=UserUpdateForm(request.POST ,instance=request.user)
        p_form=ProfileUpdateForm(request.POST ,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            string='Your Acount has been Updated   !'
            messages.success(request,string )
            return redirect ('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context={
            'u_form':u_form,
            'p_form':p_form
        }

    return render (request ,'users/profile.html',context)










