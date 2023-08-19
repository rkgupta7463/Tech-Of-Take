from django.shortcuts import render

# Create your views here.
def notify(request):
    request.session.modified = True
    return render(request,"noti/underconstnoti.html")