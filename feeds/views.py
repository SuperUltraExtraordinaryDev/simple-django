from django.shortcuts import render
from .models import *

# Create your views here.

def home_page(request):
    myinfo=PersonalInformation.objects.all()
    myabout=About.objects.all()
    myskills=Projects.objects.all()
    context={
        "info":myinfo,
        "about":myabout,
        "skills":myskills
    }
  
    return render(request,'home_page.html',context)