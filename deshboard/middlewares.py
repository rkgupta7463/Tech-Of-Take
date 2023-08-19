from django.shortcuts import render

class SiteNotify:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One time initalization")
        
    def __call__(self,request):
            print("This is execute before a view")
            response = self.get_response(request)
            print("This is execute after a view")
            return response  