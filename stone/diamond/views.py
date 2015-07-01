from django.shortcuts import render
from diamond.models import image , rings ,bangles

# Create your views here.
def home(request):
    value = image.objects.all()
    return render(request,'stone/homepage.html',{'value':value })

def ring(request):
    value = rings.objects.all()
    return render(request,'stone/products.html',{'value':value })

def bangle(request):
    value = bangles.objects.all()
    return render(request,'stone/products.html',{'value':value })

def form(request):
    return render(request,'stone/form.html')

