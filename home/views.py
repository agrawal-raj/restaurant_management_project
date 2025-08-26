from django.shortcuts import render
from .models import RestaurantInfo
# Create your views here.

def home(request):
    restaurant = RestaurantInfo.objects.first()
    return render(request, "home.html", {"restaurant_name": restaurant.name if restaurant else "Our Restaurant"})

def custom_404_test(request):
    return render(reqeust, '404.html', status=404)