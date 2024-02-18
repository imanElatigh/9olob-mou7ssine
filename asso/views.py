from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import AssociationUser, License
from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import LoginForm

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AssociationUser, License
from .forms import SignUpForm

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            name = form.cleaned_data['nom']
            license_number = form.cleaned_data['numeroLicence']
            
            if License.objects.filter(name=name, license_number=license_number).exists():
                AssociationUser.objects.create_user(email=email, password=password, nom=name, information=form.cleaned_data['information'], adresse=form.cleaned_data['adresse'], tel=form.cleaned_data['tel'], numeroLicence=license_number)
                messages.success(request, 'Account created successfully!')
                return redirect('login')
            else:
                messages.error(request, 'Association not authorized!')
        else:
            # If the form is invalid, include it in the context to display errors
            return render(request, 'sign_up.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})








from django.contrib.auth import login as auth_login

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from .forms import LoginForm

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import LoginForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                messages.error(request, ' !البريد الإلكتروني أو كلمة المرور غير صحيح  ')
        else:
            messages.error(request, 'بيانات النموذج غير صحيحة!')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})




from django.shortcuts import render
from .models import AssociationUser
from django.contrib.auth.decorators import login_required


from django.shortcuts import render
from .models import AssociationUser ,UserAssiocitionProfile


def home_view(request):
    associations = AssociationUser.objects.all()
    profile = None
    
    if request.user.is_authenticated:
        try:
            profile = UserAssiocitionProfile.objects.get(user_association=request.user)
        except UserAssiocitionProfile.DoesNotExist:
            messages.error(request, 'Your profile does not exist!')
            # Traiter ce cas comme vous le souhaitez

    context = {'associations': associations, 'profile': profile}
    return render(request, 'home.html', context)



from django.shortcuts import render

from django.shortcuts import render
from .models import AssociationUser

def index(request):
    association_users = AssociationUser.objects.all()
    return render(request, 'index.html', {'association_users': association_users})






# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth import authenticate, login as auth_login
# from .forms import SignUpForm, LoginForm
# from django.contrib.auth.decorators import login_required
# from .models import AssociationUser

# def sign_up(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             name = form.cleaned_data['nom']
#             license_number = form.cleaned_data['numeroLicence']
            
#             if License.objects.filter(name=name, license_number=license_number).exists():
#                 AssociationUser.objects.create_user(email=email, password=password, nom=name, information=form.cleaned_data['information'], adresse=form.cleaned_data['adresse'], tel=form.cleaned_data['tel'], numeroLicence=license_number)
#                 messages.success(request, 'Account created successfully!')
#                 return redirect('login')
#             else:
#                 messages.error(request, 'Association not authorized!')
#         else:
#             return render(request, 'sign_up.html', {'form': form})
#     else:
#         form = SignUpForm()
#     return render(request, 'sign_up.html', {'form': form})

# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
            
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 auth_login(request, user)
#                 messages.success(request, 'Logged in successfully!')
#                 return redirect('profile')
#             else:
#                 messages.error(request, 'Invalid email or password!')
#         else:
#             messages.error(request, 'Invalid form data!')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})

# @login_required
def profile(request):
    association = request.user
    context = {'association': association}
    return render(request, 'profile.html', context)

# def home_view(request):
#     association_name = request.user.nom if request.user.is_authenticated else "Association Name"
#     context = {'association_name': association_name}
#     return render(request, 'home.html', context)

