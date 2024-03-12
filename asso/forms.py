from django import forms
from .models import AssociationUser

from django import forms

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    profile_image = forms.ImageField(required=False)

    class Meta:
        model = AssociationUser
        fields = ['email', 'password', 'nom', 'information', 'adresse', 'tel', 'numeroLicence', 'profile_image','another_image']


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter title'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter content'})
        self.fields['image'].widget.attrs.update({'class': 'form-control-file'})
