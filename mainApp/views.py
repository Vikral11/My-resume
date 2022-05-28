from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    if (request.method=="POST"):
        contact= contactus()
        contact.name= request.POST.get("contactName")
        contact.email= request.POST.get("contactEmail")
        contact.subject= request.POST.get("contactSubject")
        contact.message= request.POST.get("contactMessage")
        contact.save()

    return render(request, "index.html")
    
