import email

from django.shortcuts import render

from blog.forms import EmailForm


def h404(request):
    return render(request,"h404.html",context={})

def about(request):
    return render(request,"about.html",context={})

def cart(request):
    return render(request,"cart.html",context={})
def checkout(request):
    return render(request,"checkout.html",context={})

def contact(request):
    form = EmailForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
      EmailForm.save()
    return render(request,"contact.html",context={})


def index(request):
    return render(request,"index.html",context={})

def index_2(request):
    return render(request,"index_2.html",context={})
def single_news(request):
    return render(request,"single_news.html",context={})

def single_product(request):
    return render(request,"single_product.html",context={})


def news(request):
    return render(request,"shop.html",context={})

def shop(request):
    return render(request,"shop.html",context={})
# Create your views here.
