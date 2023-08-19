from django.shortcuts import render, redirect
from blog.models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import os
from .forms import *

# From here all functions


# @login_required(login_url="signin")
def BlogHome(request):
    context = {}
    # BlogDB = BlogDis.objects.all()
    BlogShDB = BlogPost.objects.order_by('-date_time')  # [0:4]
    BlogSh = BlogPost.objects.all()[0:4]
    commentDB=CommentModel.objects.all()
        # this logic for pagination
    paginator = Paginator(commentDB, 4)
    page_numer = request.GET.get('page')
    CDBDatafinal = paginator.get_page(page_numer)
    totalpage = CDBDatafinal.paginator.num_pages
    fm=CommentFm()
    if request.method=='POST':
        fm=CommentFm(request.POST)
        if fm.is_valid():
            fm.save()
            fm=CommentFm()
            messages.success(request,"Thanks for your comments!")
            return redirect('Blog')
        else:
            fm=CommentFm()

    # this logic for pagination
    paginator = Paginator(BlogShDB, 10)
    page_numer = request.GET.get('page')
    BlogDatafinal = paginator.get_page(page_numer)
    totalpage = BlogDatafinal.paginator.num_pages

    context = {
        'BlDB': BlogSh,
        'BlogSh': BlogDatafinal,
        'lastpage': totalpage,
        'totalpagelist': [n+1 for n in range(totalpage)],
        'form':fm,
        'CDB': CDBDatafinal,
        'lastpage': totalpage,
        'totalpagelist': [n+1 for n in range(totalpage)],

    }
    for i in BlogShDB:
        print(i.web_link)
    return render(request, "blog_temp/Blog.html", context)


##viewadmin funcrion
@login_required(login_url="signin")
def viewadmin(request):
    if request.user.is_superuser or request.user.is_staff:
        context = {}
    # BlogDB = BlogDis.objects.all()
    BlogShDB = BlogPost.objects.all()  # [0:4]
    BlogSh = BlogPost.objects.all()[0:4]
    commentDB=CommentModel.objects.all()
        # this logic for pagination
    paginator = Paginator(commentDB, 4)
    page_numer = request.GET.get('page')
    CDBDatafinal = paginator.get_page(page_numer)
    totalpage = CDBDatafinal.paginator.num_pages
    fm=CommentFm()
    if request.method=='POST':
        fm=CommentFm(request.POST)
        if fm.is_valid():
            fm.save()
            fm=CommentFm()
            messages.success(request,"Thanks for your comments!")
        else:
            fm=CommentFm()

    # this logic for pagination
    paginator = Paginator(BlogShDB, 10)
    page_numer = request.GET.get('page')
    BlogDatafinal = paginator.get_page(page_numer)
    totalpage = BlogDatafinal.paginator.num_pages

    context = {
        'BlDB': BlogSh,
        'BlogSh': BlogDatafinal,
        'lastpage': totalpage,
        'totalpagelist': [n+1 for n in range(totalpage)],
        'form':fm,
        'CDB': CDBDatafinal,
        'lastpage': totalpage,
        'totalpagelist': [n+1 for n in range(totalpage)],

    }
    return render(request,"blog_temp/viewblog.html",context)

@login_required(login_url="signin")
def BlgNewAdd(request):
    if request.user.is_authenticated:
        fm = BlogSh()
        if request.method == 'POST':
            fm = BlogSh(request.POST, request.FILES)
            # Get the posted form
            if fm.is_valid():
                fm.save()
                messages.success(request, "Blog has created!!")
                fm = BlogSh()
                return redirect('dashboard')
        else:
            return render(request, "blog_temp/add.html", {'form': fm})
    else:
        return redirect("signin")


#filter blogs
#@login_required(login_url="signin")
def blogFliter1(request):
    context = {}
    BlogShDB = BlogPost.objects.order_by('-date_time')
    BlogSh = BlogPost.objects.all()[0:4]

    # this logic for pagination
    paginator = Paginator(BlogShDB, 10)
    page_numer = request.GET.get('page')
    BlogDatafinal = paginator.get_page(page_numer)
    totalpage = BlogDatafinal.paginator.num_pages

    context = {
        'BlDB': BlogSh,
        'BlogSh': BlogDatafinal,
        'lastpage': totalpage,
        'totalpagelist': [n+1 for n in range(totalpage)],
    }
    return render(request, "blog_temp/Blogfliter.html", context)

#@login_required(login_url="signin")
def blogFliter2(request):
    context = {}
    BlogShDB = BlogPost.objects.order_by('date_time')
    BlogSh = BlogPost.objects.all()[0:4]

    # this logic for pagination
    paginator = Paginator(BlogShDB, 10)
    page_numer = request.GET.get('page')
    BlogDatafinal = paginator.get_page(page_numer)
    totalpage = BlogDatafinal.paginator.num_pages

    context = {
        'BlDB': BlogSh,
        'BlogSh': BlogDatafinal,
        'lastpage': totalpage,
        'totalpagelist': [n+1 for n in range(totalpage)],
    }
    return render(request, "blog_temp/Blogfliter.html", context)


@login_required(login_url="signin")
def BlgEdit(request, pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            Pi = BlogPost.objects.get(id=pk)
            updata = BlogSh(request.POST, request.FILES ,instance=Pi)
            if updata.is_valid:
                updata.save()
                messages.success(request, "Blog has updated!!")
                return redirect('dashboard')
        else:
            Pi = BlogPost.objects.get(id=pk)
            updata = BlogSh(instance=Pi)

            return render(request, "blog_temp/update.html", {'BlogDB': updata})
    else:
        return redirect("signin")


# delete function
@login_required(login_url="signin")
def delete(request, pk):
    if request.user.is_authenticated:
        # if request.method == 'POST':
        member = BlogPost.objects.get(id=pk)
        member.delete()
        messages.success(request, "Blog has deleted!!")
        return redirect("dashboard")
    else:
        return redirect("signin")


def DetailBlog(request, pk):
    if request.user.is_authenticated:
        BlogDB = BlogPost.objects.get(pk=pk)

        context={
            'BlogDB': BlogDB,
        }
        return render(request, "blog_temp/details.html",context)
    else:
        return redirect("signin")
