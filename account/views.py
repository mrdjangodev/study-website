import email
from multiprocessing import AuthenticationError
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from . models import User
from . forms import RegisterForm

# Create your views here.

def register_login_page(request):
    form = RegisterForm()
    page = 'login'
    context = {
        'form': form,
        'page': page,
    }
    return render(request, 'auth_template/auth_index.html', context)


def register_login_view(request, data):
    
    # register section
    form = RegisterForm()
    page=''
    if request.POST and data == "registration":
        print('registration')
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.warning(request, f"{form.errors}")

    
    # login section
    if data == "login_act":
        page = 'login'
  
        if request.method == "POST":
            email = request.POST.get('email').lower()
            password = request.POST.get('password')
            try:
                user = User.objects.get(email=email)
            except:
                messages.error(request, "User doesn't exist")
                
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                login(request, user)    
                return redirect('home')
            else:
                messages.error(request, "User or password wrong")
            
    context = {
        'form': form,
        'page': page,
    }
    return render(request, 'auth_template/auth_index.html', context)


# @login_required(login_url='register_login_page')
def logout_view(request):
    user = request.user
    logout(request)
    return redirect('home')

@login_required(login_url='register_login_page')
def password_change_view(request):
    page = 'change_password'
    context = {
        'page': page
    }
    return render(request, 'dashboard_templates/dashboard-password-change.html', context)


def change_user_info(request):
    user = request.user
    if request.POST:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        bio = request.POST['bio']
        image = request.FILES.get('image')
        phone_number = request.POST['phone_number']
        user.first_name = first_name
        user.last_name = last_name
        user.username = user_name
        user.bio = bio
        user.avatar = image
        user.phone_number = phone_number
        user.save()
        # except:
        #     print("Something went wrong")
    page = 'change_user_info'
    context = {
        'user': user,
        'page': page,
    }
    return render(request, 'dashboard_templates/dashboard-password-change.html', context)

