from django.shortcuts import render , HttpResponseRedirect
from diamond.models import image , rings ,bangles ,contact
from diamond.forms import contactform
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
    if request.method == "POST":
        form = contactform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/form', {'success': 'Contact Added'})
        else:
            return render(request, 'stone/form.html', {'form': form})
    else:
        form = contactform()
        return render(request, 'stone/form.html', {'form': form })
