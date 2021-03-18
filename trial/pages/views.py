from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse #html kodu çalıştırmak için

def home_view(request, *args, **kwargs): #home page create

    return render(request, "home.html", {})

"""
def contact_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Contact Page</h1>")
	return render(request, "contact.html", {})
"""