from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import *
from blog.models import *
from .forms import *
from django.contrib import messages

# Create your views here.
# @login_required(login_url="signin")


def learning(request):
    request.session.modified = True
    curdata = CourseLearn.objects.all()
    # this logic is for fliter search
    if request.method == "GET":
        st = request.GET.get('search-item')
        if st != None:
            curdata = CourseLearn.objects.filter(title__icontains=st)

    if st == None:
        curdata = CourseLearn.objects.all()
    print("This is course name :- ",st)
    # this logic for pagination
    paginator = Paginator(curdata, 4)
    page_numer = request.GET.get('page')
    CourseDatafinal = paginator.get_page(page_numer)
    totalpage = CourseDatafinal.paginator.num_pages

    context = {
        'course': CourseDatafinal,
        'lastpage': totalpage,
        'totalpagelist': [n+1 for n in range(totalpage)],
        'courseName':st
    }
    return render(request, "learnTemp/learntemplates.html", context)


# admin view course
def viewadmin(request):
    request.session.modified = True
    if request.user.is_superuser or request.user.is_staff:
        curdata = CourseLearn.objects.all()
    # this logic is for fliter search
    if request.method == "GET":
        st = request.GET.get('search-item')
        if st != None:
            curdata = CourseLearn.objects.filter(title__icontains=st)

    if st == None:
        curdata = CourseLearn.objects.all()

    # this logic for pagination
    paginator = Paginator(curdata, 4)
    page_numer = request.GET.get('page')
    CourseDatafinal = paginator.get_page(page_numer)
    totalpage = CourseDatafinal.paginator.num_pages

    context = {
        'course': CourseDatafinal,
        'lastpage': totalpage,
        'totalpagelist': [n+1 for n in range(totalpage)],
        'courseName':st,
    }
    return render(request, "learnTemp/learnview.html", context)
# add learning tutorial


def AddLearning(request):
    if request.user.is_authenticated:
        request.session.modified = True
        fm = AddLearn()
        if request.method == 'POST':
            fm = AddLearn(request.POST, request.FILES)
            # Get the posted form
            if fm.is_valid():
                fm.save()
                messages.success(request, "Course has created!!")
                return redirect('dashboard')
        else:
            fm = AddLearn()
            return render(request, "learnTemp/addlrn.html", {'form': fm})
    else:
        return redirect("signin")

# update learning


def updatecourse(request, pk):
    if request.user.is_authenticated:
        request.session.modified = True
        if request.user.is_superuser:
            pi = CourseLearn.objects.get(id=pk)
            fm = AddLearn(instance=pi)
            if request.method == "POST":
                fm = AddLearn(request.POST, request.FILES, instance=pi)
                if fm.is_valid():
                    fm.save()
                    messages.success(request, "Course has updated!")
                    return redirect("dashboard")
            else:
                return render(request, "learnTemp/courseupdate.html", {'form': fm})
    else:
        return redirect("signin")

# delete function


def deletecourse(request, pk):
    if request.user.is_authenticated:
        request.session.modified = True
        if request.user.is_superuser:
            coursedel = CourseLearn.objects.get(id=pk)
            coursedel.delete()
            messages.success(request, "Course has deleted!")
            return redirect("dashboard")
    else:
        return redirect("signin")


def trending(request):
    request.session.modified = True
    curdata = TrendingModel.objects.all()
    # this logic is for fliter search
    if request.method == "GET":
        st = request.GET.get('search-trend')
        if st != None:
            curdata = TrendingModel.objects.filter(title__icontains=st)
    if st == None:
        curdata = TrendingModel.objects.all()

    # # this logic is for fliter search
    if request.method == "GET":
        st = request.GET.get('search-trend')
        if st != None:
            curdata = TrendingModel.objects.filter(title__icontains=st)

    if st == None:
        curdata = TrendingModel.objects.all()

    # this logic for pagination
    paginator = Paginator(curdata, 6)
    page_numer = request.GET.get('page')
    trendDatafinal = paginator.get_page(page_numer)
    totalpage = trendDatafinal.paginator.num_pages

    context = {
        'course': trendDatafinal,
        'lastpage': totalpage,
        'totalpagelist': [n+1 for n in range(totalpage)],
    }
    return render(request, "learnTemp/trendingit.html", context)
