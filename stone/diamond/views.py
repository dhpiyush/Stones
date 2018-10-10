from django.shortcuts import render , HttpResponseRedirect
from django.core.mail import EmailMessage
from diamond.models import image, rings, bangles, earrings, necklaces, pendants, contact
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

def earring(request):
    value = earrings.objects.all()
    return render(request,'stone/products.html',{'value':value })

def necklace(request):
    value = necklaces.objects.all()
    return render(request,'stone/products.html',{'value':value })

def pendant(request):
    value = pendants.objects.all()
    return render(request,'stone/products.html',{'value':value })

# def form(request):
#     if request.method == "POST":
#         form = contactform(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/form', {'success': 'Contact Added'})
#         else:
#             return render(request, 'stone/form.html', {'form': form})
#     else:
#         form = contactform()
#         return render(request, 'stone/form.html', {'form': form })


def form(request):
    if request.method == "POST":
        form = contactform(data=request.POST)
        body = ''
        if form.is_valid():
            form.save()
            body = ' Name: ' + form.cleaned_data['name'] + '\n Number: ' + form.cleaned_data['number'] + ' \n Email: ' + form.cleaned_data['email'] + ' \n Message: ' + form.cleaned_data['message']
            email = EmailMessage('New Contact', body, to=['piyushdh94@gmail.com'])
            email.send()
            return HttpResponseRedirect('/successPage')
    else:
        form = contactform()
    return render(request, 'stone/form.html', {'form': form})



def success(request):
    return render(request,'stone/successPage.html')
