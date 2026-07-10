from django.shortcuts import render
from .models import FoodItem


def food_list(request):
    food_items = FoodItem.objects.all().order_by('expiration_date')
    return render(request, 'pantry/food_list.html', {'food_items': food_items})