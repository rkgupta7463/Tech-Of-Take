from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from home.models import InterestArea

# @login_required(login_url="signin")
def AboutMe(request):
    request.session.modified = True
    rm=Resume.objects.all()
    InterestImg = InterestArea.objects.all()
    context={
        'rm':rm,
        'InterestImg':InterestImg,
    }
    return render(request, "personal/about.html", context)
# Create your views here.
