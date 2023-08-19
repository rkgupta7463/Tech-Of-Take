from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import *
from django.contrib import messages
# Create your views here.


@login_required(login_url="signin")
def Testiminal(request):
    if request.user.is_authenticated:
        request.session.modified = True
        TDB = TestiminalModel.objects.all()
        context = {'TDB': TDB}
        print(TDB)
        user = request.user
        if request.method == 'POST':
            name = request.POST.get('username')
            email = request.POST.get('email')
            phone = request.POST.get('phone_no')
            message = request.POST.get('message')
            profession = request.POST.get('profession')
            # print(TestiminalModel)
            TDB = TestiminalModel(cname=name, cemail=email,
                                  cphone=phone, ctitle=profession, cfeedback=message)
            TDB.save()
            subject = "welcome to Rishu Devloper & Blogger"
            message = f"Hi {user.username}, Thank you for given feedback. 🤞Good Luck for your future🤞from Rishu developer & blogger company"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail(subject, message, email_from, recipient_list)
            messages.success(request, 'Thanks for Your feedback')
        return render(request, "testim/testiminal.html", context)
    else:
        return redirect("signin")