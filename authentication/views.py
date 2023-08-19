from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import socket
from django.http import *
from django.contrib.auth.forms import *
from .forms import *
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
import re
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


def is_valid_password(password):
    # Check password length
    if len(password) < 8 or len(password) > 16:
        return False

    # Check for at least one alphabet, one special symbol, and one numerical
    if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$', password):
        return False

    return True

def is_valid_username(username):
    return re.match(r'^[a-zA-Z0-9_]+$', username)

def is_valid_name(name):
    return re.match(r'^[a-zA-Z]+$', name)

def is_valid_email(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


def signinUser(request):
    if request.user.is_authenticated:
        return redirect("signin")

    context = {}

    try:
        if request.method == 'POST':
            fname = request.POST.get("fname")
            lname = request.POST.get("lname")
            email = request.POST.get("email")
            username = request.POST.get("username")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")

            if not is_valid_username(username):
                messages.error(request, "Invalid username format!")
                return redirect('signup')

            if not is_valid_name(fname) or not is_valid_name(lname):
                messages.error(request, "Invalid first name or last name format!")
                return redirect('signup')

            if not is_valid_email(email):
                messages.error(request, "Invalid email format!")
                return redirect('signup')

            if not is_valid_password(password1):
                messages.error(request, "Invalid password format! Password should have at least 8 characters, maximum 16 characters, one alphabet, one special symbol, and one numerical.")
                return redirect('signup')

            if password1 != password2:
                messages.error(request, "Passwords do not match!")
                return redirect('signup')

            if User.objects.filter(username=username).first():
                messages.error(request, "This username is already taken! Please login with user id!")
                return redirect('signup')

            if User.objects.filter(email=email).first():
                messages.error(request, "This email is already taken! Please login with user id")
                return redirect('signup')

            user = User.objects.create_user(
                username=username, email=email, password=password1, first_name=fname, last_name=lname)
            user.save()
            group = Group.objects.get(name="users")
            user.groups.add(group)
            login(request, user)

            messages.success(request, "Welcome {}🎉".format(request.user.get_short_name()))

            subject = "❤️Welcome to TechTake Company🎉"
            message = f"Hi {user.first_name}, Thank you for registering on Rishu Developer & Blogger. Here you can gather knowledge about basic blogs and programming topics such as HTML, JS, CSS, PYTHON, DJANGO, JAVA, WEB DEVELOPMENT, and more. If you encounter any problems, feel free to contact us at rishukumargupta8409@gmail.com."
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            send_mail(subject, message, email_from, recipient_list, fail_silently=False)

            return redirect("Home")

    except socket.gaierror:
        return HttpResponseServerError("Internet connection error😒😒")

    return render(request, "auth/signup.html", context)


##from here login code
def loginUser(request):
    if request.user.is_authenticated:
        return redirect("Home")
    context = {}
    try:
        # if not socket.error:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request,"Welcome back {}🎉".format(request.user.get_short_name()))
                return redirect("Home")
            else:
                messages.warning(request, "User or password is not correct!")

        return render(request, "auth/login.html", context)

        # else:
    except socket.error:
        return HttpResponseServerError("Your Internet connection is very slow😒😒")

def forget(request):
    if request.POST == 'POST':
        form = ForgetPass(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password has changed Successfully!!")
    else:
        form = ForgetPass(user=request.user)

    context = {'form': form}
    return render(request, 'auth/forgetpass.html', context)

# logout function
@login_required(login_url="signin")
def logOutUser(request):
    try:
        logout(request)
        messages.success(request,"Logged Out successfully!")
        return redirect("Home")
    except socket.gaierror:
        return HttpResponseServerError("Internet connection error")
