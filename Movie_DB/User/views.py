from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
from User.forms import Userform
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User
# Create your views here.
def edit_user(request):
    user=request.user
    form=Userform(instance=user)
    if request.method=='POST':
        form=Userform(request.POST,instance=user)
        if form.is_valid:
            form.save()
            return userprofile(request)
    return render(request,'editprofile.html',{'edit':form})

def edit_password(request):
    user=request.user
    if request.method=='POST':
        password=request.POST['password']
        confirm=request.POST['confirm']
        if password == confirm:
            user.password.update(password)
    return render(request,'editprofile.html')

class Update_User(UpdateView):
    model=User
    template_name='userprofile.html'
    fields=['username','password']
    success_url=reverse_lazy('User:userprofile')

def userprofile(request):
    try:
        user=request.user
        user.save()
        return redirect(request,'Movie:home')
    except:
        pass
    return render(request,'editprofile.html',{'user':user})

class Password_change(PasswordChangeView):
    form_class=""
    success_url = reverse_lazy()

def password_success(request):
    return render(request,'password_changed.html')
