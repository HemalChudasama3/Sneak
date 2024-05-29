from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from login.models import FormData
from shop.models import Shoe

def home(request):
    return render(request, "index.html")

def shop(request):
    return render(request, "shop.html")

def about(request):
    return render(request, "about.html")

def login(request):
    return render(request, "login.html")

def profile(request):
    return render(request, "profile.html")

def saveLogin(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')

        # Save login information
        lgn = FormData(name=name, email=email, mobile=mobile, address=address)
        lgn.save()
    return render(request, "login.html")

def shop(request):
    shoes = Shoe.objects.all()
    return render(request, 'shop.html', {'shoes': shoes})

def shoe_detail(request, shoe_id):
    shoe = get_object_or_404(Shoe, pk=shoe_id)
    return render(request, 'shoe_detail.html', {'shoe': shoe})