from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from store.models import *


# Create your views here.
def index(request):
    return render(request, 'cars/index.html')


@login_required(login_url='login')
def shop(request):
    category = Category.objects.filter(status=0)
    context = {'category': category}
    return render(request, "store/shop.html", context)

def shopview(request,slug):
    if Category.objects.filter(slug=slug, status=0):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products': products, 'category':category}
        return render(request, "store/shopview.html", context)
    else:
        # messages.warning(request,"No Vehicles for sale under this brand")
        return redirect('shop')

def productview(request,cate_slug,prod_slug):
    if Category.objects.filter(slug=cate_slug, status=0):
        if Product.objects.filter(slug=prod_slug, status=0):
            products = Product.objects.filter(slug=prod_slug, status=0).first()
            context = {'products': products}
        else:
            # messages.error(request, "No such car found")
            return redirect('shop')
    else:
        # messages.error(request,"No such brand vehicles found")
        return redirect('shop')
    return render(request, 'store/productview.html',context)

def about(request):
    return render(request, 'cars/about.html')


