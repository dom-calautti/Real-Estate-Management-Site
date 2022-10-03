from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import province_choices,bedroom_choices,price_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)[:3]
    
    context = {
        'listings' : listings ,  
        'province_choices' : province_choices,
        'bedroom_choices' : bedroom_choices,
        'price_choices' : price_choices   
    }
    
    return render(request,'pages/index.html', context) 

def about(request):
    realtors = Realtor.objects.all().order_by('-hire_date')
    mvp = realtors.filter(is_MVP =True)
    
    context = {
        'mvp' : mvp,
        'realtors' : realtors
    }
    
    return render(request, 'pages/about.html', context) #get
