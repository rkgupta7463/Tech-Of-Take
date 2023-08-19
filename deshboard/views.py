from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from learn.models import *
from django.core.paginator import Paginator
from blog.models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError


# Create your views here.
@login_required(login_url="signin")
def desh(request):
    if request.user.is_authenticated:
        request.session.modified = True
        user_data = User.objects.get(username=request.user.username)
        view_img = ProfileUserImg.objects.filter(profile=user_data).first()  # Get the first image if exists
        allcurdata = CourseLearn.objects.all()[:8]
        curdata = CourseLearn.objects.all()
        users = User.objects.all()
        BlogSh = BlogPost.objects.all()[:4]
        post = BlogPost.objects.filter(author=request.user)
        # this logic for pagination
        paginator = Paginator(curdata, 4)
        page_numer = request.GET.get('page')
        CourseDatafinal = paginator.get_page(page_numer)
        totalpage = CourseDatafinal.paginator.num_pages
        user = request.user
        full_name = user.get_full_name()
        print(full_name)
        context = {
            'user': user_data,
            'full_name': full_name,
            'course': CourseDatafinal,
            'lastpage': totalpage,
            'totalpagelist': [n+1 for n in range(totalpage)],
            'post': post,
            'users': users,
            'BlogSh':BlogSh,
            'allcurdata':allcurdata,
            'view_img':view_img,
        }
        return render(request, "desh/desh.html", context)
    else:
        return redirect("signin")

@login_required(login_url="signin")
def profile_view(request, pk):
    if request.user.is_authenticated:
        request.session.modified = True
        vp = User.objects.get(id=pk)
        view_img = ProfileUserImg.objects.filter(profile=vp).first()  # Get the first image if exists

    if request.method == 'POST':
        pro_img = ProfileUserImg(profile=vp)  # Use profile=vp instead of profile_name=vp
        if 'upload' in request.FILES:
            uploaded_file = request.FILES['upload']
            if uploaded_file.size > 5 * 1024 * 1024:  # 5MB in bytes
                messages.error(request, "File size should not exceed 5MB.")
            else:
                if view_img:  # Update the existing image if it exists
                    view_img.file = uploaded_file
                    view_img.save()
                    messages.success(request, "Profile image has been updated!")
                else:  # Upload a new image if it doesn't exist
                    pro_img.file = uploaded_file
                    pro_img.save()
                    messages.success(request, "Profile image has been uploaded!")
                return redirect(reverse("profileview", args=[pk]))
        else:
            messages.error(request, "No file was uploaded.")

    return render(request, "desh/profileview.html", {'vp': vp, 'view_img': view_img})



# User list
@login_required(login_url="signin")
def usersList(request):
    if request.user.is_superuser:
        if request.user.is_authenticated:
            request.session.modified = True
            user_data = User.objects.get(username=request.user.username)
            users = User.objects.all()
            user = request.user
            full_name = user.get_full_name()
            context = {'user_data': user_data,
                       'users': users, 'full_name': full_name}
            return render(request, "desh/userslist.html", context)
        else:
            return redirect("signin")
    else:
        return redirect("dashboard")

# user profile's edit
@login_required(login_url="signin")
def usersproEdit(request, pk):
    if request.user.is_authenticated:
        request.session.modified = True
        pi = User.objects.get(id=pk)
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm = EditAdminProfile(request.POST, instance=pi)
            else:
                fm = user_profile_change(request.POST, instance=pi)
            if fm.is_valid():
                messages.success(request, "Profile has updated!!")
                fm.save()
                return redirect("userslist")
        else:
            if request.user.is_superuser == True:
                fm = EditAdminProfile(instance=pi)
            else:
                fm = user_profile_change(instance=pi)
        context = {'form': fm, }
        return render(request, "desh/profileEdit.html", context)
    else:
        return redirect("signin")

# profile Edit function


@login_required(login_url="signin")
def EditProfile(request):
    if request.user.is_authenticated:
        request.session.modified = True
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm = EditAdminProfile(request.POST, instance=request.user)
            else:
                fm = user_profile_change(request.POST, instance=request.user)
            if fm.is_valid():
                messages.success(request, "Profile has updated!!")
                fm.save()
                return redirect("dashboard")
        else:
            if request.user.is_superuser == True:
                fm = EditAdminProfile(instance=request.user)
            else:
                fm = user_profile_change(instance=request.user)
        context = {'form': fm, }
        return render(request, "desh/profileEdit.html", context)
    else:
        return redirect("signin")


# userAdd function
@login_required(login_url="signin")
def usersAddFun(request):
        if request.user.is_authenticated:
            request.session.modified = True
            if request.user.is_superuser:
                if request.method == 'POST':
                    fm = usersAdd(request.POST)
                    pass1 = request.POST['password1']
                    pass2 = request.POST['password2']
                    if pass1 != pass2:
                        messages.warning(request, "Password don't matching!")
                    else:
                        if fm.is_valid():
                            fm.save()
                            messages.success(
                                request, 'User has created successfully')
                            return redirect('userslist')
                else:
                    fm = usersAdd()
                context = {
                    'form': fm
                }
                return render(request, "desh/userAdd.html", context)
            else:
                return HttpResponse("Not avalible!")
        else:
            return redirect("signin")

# user delete by admin

@login_required(login_url="signin")
def userdelete(request, pk):
    if request.user.is_superuser:
        request.session.modified = True
        udelete = User.objects.get(id=pk)
        udelete.delete()
        messages.success(request, 'User has deleted successfully')
        return redirect("userslist")

# user password change

@login_required(login_url="signin")
def UserPassChange(request):
    if request.user.is_authenticated:
        request.session.modified = True
        user = request.user
        if request.method == 'POST':
            fm = UserPassChangewithold(user, request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, "Password Changed!")
                return redirect("dashboard")
        else:
            # messages.warning(request,"Some issue occuring!")
            fm = UserPassChangewithold(user=request.user)
        context = {'form': fm}
        return render(request, "desh/userpasschange.html", context)
    else:
        return redirect("signin")