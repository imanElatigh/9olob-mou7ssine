from django import forms
from .models import AssociationUser

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = AssociationUser
        fields = ['email', 'password', 'nom', 'information', 'adresse', 'tel', 'numeroLicence']

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
