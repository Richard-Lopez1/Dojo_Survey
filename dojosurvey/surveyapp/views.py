# from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, HttpResponse
def index(request):
    context = {
        'menu_item': ['Chum made by Zaur', 'Chicken Tacos', 'Steak', 'Cheese Burger']
    }
    return render(request, 'index.html', context)

def submission(request):
    print('Welcome to thank you page')
    print(request.POST)
    print(request.POST['user_name'])
    print(request.POST['menu_item'])
    
    context = {
        'customer_from_form': request.POST['user_name'],
        'food_from_form': request.POST['menu_item']
    }


    return render(request, 'confirm.html', context)
