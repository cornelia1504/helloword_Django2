from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

from helloworldapp.models import Person

def helloworld1(request):
     name = "Bogo"
     html = "<html><body>Hello World! from {name}</body></html>".format(name=name)
     return HttpResponse(html)

def helloworld2(request,):
    return render(request, "helloworld1.html", {"name" : "Bogo"})

def helloworld3(request, name):  # helloworld2/Bogo
    return render(request, "helloworld1.html", {"name" : name})

def helloworld4(request, name):  # hierachical templates
    return render(request, "helloworld3.html", {"name" : name})

###############################################################################
# Django 2
###############################################################################

def helloworld5(request,):  # read database
    return render(request, "helloworld4.html", {"person_lst": Person.objects.all().values()})

def helloworld6(request,):  # read css
    return render(request, "helloworld5.html")

def helloworld7(request,):  # internal link to helloworld8
    return render(request, "helloworld6.html")

def helloworld8(request,):  # internal link to helloworld7
    return render(request, "helloworld7.html")