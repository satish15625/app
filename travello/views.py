from django.shortcuts import render
from .models import Destinations
from .models import Banner
from .models import Testimonials
from .models import News_Details
from .models import offersDetails
from .models import aboutUs

# Create your views here.

# index file function
def index(request):

    dests = Destinations.objects.filter(published=True).order_by('-date')[0:3]
    banner = Banner.objects.all()
    testimonials = Testimonials.objects.all()
    new_details = News_Details.objects.all()
    offer_details = offersDetails.objects.all()

    return render(request,"index.html",{'dests':dests,'banner':banner,'testimonials':testimonials,'new_details':new_details, 'offer_details':offer_details})

#about us page function
def about(request):
    
    about = aboutUs.objects.all()

    return render(request,"about.html",{'about':about})

def news(request):
    return render(request,"news.html")

def contact(request):
    return render(request,"contact.html")

def destinations(request):
     dests = Destinations.objects.all()
     new_details = News_Details.objects.all()
     return render(request,'destinations.html',{'dests':dests,'new_details':new_details})