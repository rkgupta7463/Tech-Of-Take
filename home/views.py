from django.shortcuts import render, redirect
from blog.models import *
from .models import *
from testiminal.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages


# @login_required(login_url="signin")
def Home(request):
    user=request.user
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # print(TestiminalModel)
        TDB = TestiminalModel(cname=name, cemail=email, ctitle=subject, cfeedback=message)
        TDB.save()
        subject = "welcome to TechTake Company🎉"
        message = f"Hi {name}, Thank you for given feedback. 🤞Good Luck for your future🤞from Rishu developer & blogger company.\nHave good days {name}"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email,]
        send_mail(subject, message, email_from, recipient_list)
        messages.success(request, 'Thanks for Your feedback🙏')
        return redirect('/')

    if request.user.is_authenticated:
        user=request.user
        full_name=user.get_full_name()
    else:
        full_name=None
    InterestImg=InterestArea.objects.all()
    TDB=TestiminalModel.objects.all()
    ProjModel=ProjectModel.objects.all()
    FeatureDB=FeartureSection.objects.all()
    BlogDB = BlogPost.objects.order_by('-date_time')[:6]
    print(BlogDB)

    context={
        'InterestImg':InterestImg,
        'TDB':TDB,
        'proj':ProjModel,
        'Feat':FeatureDB,
        'full_name':full_name,
        'BlogSh':BlogDB,
    }
    return render(request, "home_temp/index.html", context)
    # else:
    #     return redirect("signin")


def showmore(request, pk):
    InterestImg = InterestArea.objects.get(pk=pk)
    print(InterestArea)
    return render(request, "home_temp/showinterest.html", {'Int': InterestImg})


def showproject(request, pk):
    Proj = ProjectModel.objects.get(pk=pk)
    context = {'Proj': Proj}
    return render(request, "home_temp/showproject.html", context)


def cruddata(request):

    user=request.user
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # print(TestiminalModel)
        TDB = TestiminalModel(cname=name, cemail=email, ctitle=subject, cfeedback=message)
        TDB.save()
        subject = "️Welcome to TechTake Company🎉"
        message = f"Hi {name}, Thank you for given feedback. 🤞Good Luck for your future🤞from Rishu developer & blogger company.\nHave good days {name}"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]
        send_mail(subject, message, email_from, recipient_list)
        messages.success(request, 'Thanks for Your feedback')
        return redirect('/')

    if request.user.is_authenticated:
        user=request.user
        full_name=user.get_full_name()
    else:
        full_name=None
    InterestImg=InterestArea.objects.all()
    TDB=TestiminalModel.objects.all()
    FeatureDB=FeartureSection.objects.all()
    BlogDB = BlogPost.objects.order_by('-date_time')[:6]
    print(BlogDB)

    cruddb=ProjectModel.objects.get(proj_title__iexact='Crud Application')
    TDB=TestiminalModel.objects.all()
    context={
            'cruddb':cruddb,
            'TDB':TDB,
            'InterestImg':InterestImg,
            'Feat':FeatureDB,
            'BlogSh':BlogDB,
            'full_name':full_name,
    }
    return render(request, "home_temp/index.html",context)

def blogging(request):

    user=request.user
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # print(TestiminalModel)
        TDB = TestiminalModel(cname=name, cemail=email, ctitle=subject, cfeedback=message)
        TDB.save()
        subject = "️Welcome to TechTake Company🎉"
        message = f"Hi {name}, Thank you for given feedback. 🤞Good Luck for your future🤞from Rishu developer & blogger company.\nHave good days {name}"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]
        send_mail(subject, message, email_from, recipient_list)
        messages.success(request, 'Thanks for Your feedback')
        return redirect('/')

    if request.user.is_authenticated:
        user=request.user
        full_name=user.get_full_name()
    else:
        full_name=None
    InterestImg=InterestArea.objects.all()
    TDB=TestiminalModel.objects.all()
    FeatureDB=FeartureSection.objects.all()
    BlogDB = BlogPost.objects.order_by('-date_time')[:6]
    print(BlogDB)

    blogs=ProjectModel.objects.get(proj_title__iexact='Blogging Application')
    TDB=TestiminalModel.objects.all()
    context={
            'blogs':blogs,
            'TDB':TDB,
            'InterestImg':InterestImg,
            'Feat':FeatureDB,
            'BlogSh':BlogDB,
            'full_name':full_name,
    }
    return render(request, "home_temp/index.html",context)
def weather(request):

    user=request.user
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # print(TestiminalModel)
        TDB = TestiminalModel(cname=name, cemail=email, ctitle=subject, cfeedback=message)
        TDB.save()
        subject = "️Welcome to TechTake Company🎉"
        message = f"Hi {name}, Thank you for given feedback. 🤞Good Luck for your future🤞from Rishu developer & blogger company.\nHave good days {name}"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]
        send_mail(subject, message, email_from, recipient_list)
        messages.success(request, 'Thanks for Your feedback')
        return redirect('/')

    if request.user.is_authenticated:
        user=request.user
        full_name=user.get_full_name()
    else:
        full_name=None
    InterestImg=InterestArea.objects.all()
    TDB=TestiminalModel.objects.all()
    FeatureDB=FeartureSection.objects.all()
    BlogDB = BlogPost.objects.order_by('-date_time')[:6]
    print(BlogDB)

    weathers=ProjectModel.objects.get(proj_title__iexact='Weather Aplication')
    TDB=TestiminalModel.objects.all()
    context={
            'weathers':weathers,
            'TDB':TDB,
            'InterestImg':InterestImg,
            'Feat':FeatureDB,
            'BlogSh':BlogDB,
            'full_name':full_name,
    }
    return render(request, "home_temp/index.html",context)

##image uploader
def imageup(request):

    user=request.user
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # print(TestiminalModel)
        TDB = TestiminalModel(cname=name, cemail=email, ctitle=subject, cfeedback=message)
        TDB.save()
        subject = "️Welcome to TechTake Company🎉"
        message = f"Hi {name}, Thank you for given feedback. 🤞Good Luck for your future🤞from Rishu developer & blogger company.\nHave good days {name}"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]
        send_mail(subject, message, email_from, recipient_list)
        messages.success(request, 'Thanks for Your feedback')
        return redirect('/')

    if request.user.is_authenticated:
        user=request.user
        full_name=user.get_full_name()
    else:
        full_name=None
    InterestImg=InterestArea.objects.all()
    TDB=TestiminalModel.objects.all()
    FeatureDB=FeartureSection.objects.all()
    BlogDB = BlogPost.objects.order_by('-date_time')[:6]
    print(BlogDB)

    weathers=ProjectModel.objects.get(proj_title__iexact='Image Uploader')
    TDB=TestiminalModel.objects.all()
    context={
            'weathers':weathers,
            'TDB':TDB,
            'InterestImg':InterestImg,
            'Feat':FeatureDB,
            'BlogSh':BlogDB,
            'full_name':full_name,
    }
    return render(request, "home_temp/index.html",context)


#car price predictor function
def car_price_pred(request):

    user=request.user
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # print(TestiminalModel)
        TDB = TestiminalModel(cname=name, cemail=email, ctitle=subject, cfeedback=message)
        TDB.save()
        subject = "welcome️Welcome to TechTake Company🎉"
        message = f"Hi {name}, Thank you for given feedback. 🤞Good Luck for your future🤞from Rishu developer & blogger company.\nHave good days {name}"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]
        send_mail(subject, message, email_from, recipient_list)
        messages.success(request, 'Thanks for Your feedback')
        return redirect('/')

    if request.user.is_authenticated:
        user=request.user
        full_name=user.get_full_name()
    else:
        full_name=None
    InterestImg=InterestArea.objects.all()
    TDB=TestiminalModel.objects.all()
    FeatureDB=FeartureSection.objects.all()
    BlogDB = BlogPost.objects.order_by('-date_time')[:6]
    print(BlogDB)

    car_price_predictor=ProjectModel.objects.get(proj_title__iexact='Car Price Predictor')

    TDB=TestiminalModel.objects.all()
    context={
            'TDB':TDB,
            'InterestImg':InterestImg,
            'Feat':FeatureDB,
            'BlogSh':BlogDB,
            'full_name':full_name,
            'car_pred':car_price_predictor,
    }
    return render(request, "home_temp/index.html",context)