from ast import keyword
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing
from .choices import province_choices,bedroom_choices,price_choices

# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published = True) #Listing.objects.all()
    
    paginator = Paginator(listings,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    
    context = {
        'listings' : paged_listings ,   #listings
        
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id): 
    listing = get_object_or_404(Listing, pk = listing_id)
    
    context = {
        'listing' : listing
    }
    return render(request,'listings/listing.html',context)

def search(request):
    queryset_list= Listing.objects.order_by("-list_date")
    
    #Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:                           # redudant? cause two line above
            queryset_list = queryset_list.filter(description__icontains=keywords) #checks description has key
    #City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city) #case insensiive i
    
    #Province
    if 'province' in request.GET:
        province = request.GET['province']
        if province and province != 'Province (All)':
            queryset_list = queryset_list.filter(province__iexact=province)
    
    #Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            if '+' in bedrooms:
                queryset_list = queryset_list.filter(bedrooms__gte= int(bedrooms[0])) 
            elif bedrooms != 'Bedrooms (Any)':
                queryset_list =queryset_list.filter(bedrooms__iexact=bedrooms)
    #Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price and price != 'Max Price (Any)':
            queryset_list = queryset_list.filter(price__lte=price)
            
    context = {
        'province_choices' : province_choices,
        'bedroom_choices' : bedroom_choices,
        'price_choices' : price_choices,
        'queryset_list' : queryset_list,
        'values' : request.GET
   }
    return render(request, 'listings/search.html',context)