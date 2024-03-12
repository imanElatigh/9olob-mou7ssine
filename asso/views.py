from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import AssociationUser, License

from .forms import LoginForm

from .models import AssociationUser, License
from .forms import SignUpForm


from django.shortcuts import render, get_object_or_404
from .models import AssociationUser



from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.shortcuts import render

from django.shortcuts import render
from .models import AssociationUser
from django.contrib.auth import authenticate, login as auth_login
from .forms import LoginForm

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import LoginForm


from .models import AssociationUser
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm



from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import PostForm
from django.shortcuts import render
from .models import AssociationUser, Post
from django.shortcuts import render
from .models import Chatbot
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import Post
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login






def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            name = form.cleaned_data['nom']
            license_number = form.cleaned_data['numeroLicence']
            
            if License.objects.filter(name=name, license_number=license_number).exists():
                # Create the user instance
                user = AssociationUser.objects.create_user(email=email, password=password, nom=name, information=form.cleaned_data['information'], adresse=form.cleaned_data['adresse'], tel=form.cleaned_data['tel'], numeroLicence=license_number)
                
                # Handle profile image upload
                if 'profile_image' in request.FILES:
                    user.profile_image = request.FILES['profile_image']

                # Handle another image upload
                if 'another_image' in request.FILES:
                    user.another_image = request.FILES['another_image']

                user.save()
                
                return redirect('login')
            else:
                messages.error(request, '  جمعية غير مرخصة ! يمكنك التحقق من البيانات  ')
        else:
            # If the form is invalid, include it in the context to display errors
            return render(request, 'sign_up.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})






def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)
                request.session['logged_in_user'] = user.pk  # Store user ID in session
                return redirect('profile')  # Redirect to the profile page
            else:
                messages.error(request, 'الإيميل أو كلمة المرور غير صحيحين ')
        else:
            messages.error(request, 'بيانات خطأ')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})











def index(request):
    association_users = AssociationUser.objects.all()

    # Add related posts to each association user
    for user in association_users:
        user.posts = Post.objects.filter(association=user)

    return render(request, 'index.html', {'association_users': association_users})







def search_response(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        try:
            chatbot_instance = Chatbot.objects.get(question__icontains=query)
            response = chatbot_instance.response
        except Chatbot.DoesNotExist:
            response = "لا تتوفر لدي المعلومات الكافية "
        return render(request, 'search_response.html', {'response': response})
    return render(request, 'search_response.html')






def profile(request):
    user_id = request.session.get('logged_in_user')
    if user_id:
        User = get_user_model()
        user = User.objects.get(pk=user_id)
        
        # Fetch posts associated with the user
        user_posts = Post.objects.filter(association=user)
        
        return render(request, 'profile.html', {'user': user, 'user_posts': user_posts})
    else:
        # Handle case when user is not logged in
        return redirect('login')  # Redirect to login page







def create_post(request):
    user_id = request.session.get('logged_in_user')
    if user_id:
        User = get_user_model()
        user = User.objects.get(pk=user_id)
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.association = user  # Associate the post with the logged-in user
                post.save()
                return redirect('profile')  # Redirect to the profile page after successfully creating a post
        else:
            form = PostForm()
        return render(request, 'create_post.html', {'form': form})
    else:
        # Handle case when user is not logged in
        return redirect('login')  # Redirect to login page




def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.association:
        return redirect('post_detail', post_id=post.id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form, 'post': post})





def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.association:
        post.delete()
    return redirect('home')  # Redirect to the homepage or any other desired page






def association_detail(request, association_id):
    association = get_object_or_404(AssociationUser, id=association_id)
    association_posts = Post.objects.filter(association=association)
    return render(request, 'association_detail.html', {'association': association, 'association_posts': association_posts})






def association_user_detail(request, user_id):
    user = get_object_or_404(AssociationUser, pk=user_id)
    association_posts = Post.objects.filter(association=user)
    return render(request, 'association_user_detail.html', {'user': user, 'association_posts': association_posts})


