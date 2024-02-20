from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'cars/index.html')
def shop(request):
    return render(request, 'cars/shop.html')
def userreg(request):
    return render(request, 'cars/userreg.html')

def userlogin(request):
    return render(request, 'cars/userlogin.html')