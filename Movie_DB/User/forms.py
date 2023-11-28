from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

class Userform(forms.ModelForm):
    class Meta:
        model=User
        # fields='__all__'
        fields=['username','password','email']


class PasswordChangingForm(PasswordChangeForm):
    class Meta:
        model=User
        fields = '__all__'