from django.shortcuts import render
# from django.contrib.auth.models import User
from User.forms import Userform
from django.views.generic import UpdateView
from django.urls import reverse_lazy
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

def Update_User(UpdateView):
    model=User
    template_name='userprofile.html'
    fields=['username','password']
    success_url=reverse_lazy('User:userprofile')

def userprofile(request):
    user=request.user
    return render(request,'editprofile.html',{'user':user})