from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from .models import *
import socket
from django.http import *
# Create your views here.


# @login_required(login_url="signin")
def Contact(request):
    request.session.modified = True
    context = {}
    user = request.user
    try:
        if request.method == 'POST':
            username = request.POST.get('name')
            email = request.POST.get('email')
            umessage = request.POST.get('message')

            cfm=ContactModel(uname=username, uemail=email, umessage=umessage)
            cfm.save()

            subject = "welcome to Rishu's devloper & bloger"
            message = f"Hello {username}, Thank you for contacting us, Our Team will reply soon to your Question from Rishu developer & blogger company.\nEmail id : rishukumargupta8409@gmail.com"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            print(recipient_list)
            print(message)
            send_mail(subject, message, email_from, recipient_list)
            context = {'message': 'Thanks You! Our team will reply soon!'}
        return render(request, "cont/contact.html", context)
    except socket.gaierror:
        return HttpResponseServerError("Internet connection error")