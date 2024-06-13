from django.shortcuts import render, redirect
from .models import MenuItem, CateringBooking

def index(request):
    return render(request, 'catering/index.html')

def menu(request):
    items = MenuItem.objects.all()
    return render(request, 'catering/menu.html', {'items': items})

def book_catering(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        event_date = request.POST.get('event_date')
        menu_items = request.POST.getlist('menu_items')
        special_requests = request.POST.get('special_requests')

        booking = CateringBooking(
            customer_name=name,
            customer_email=email,
            event_date=event_date,
            special_requests=special_requests
        )
        booking.save()
        for item_id in menu_items:
            booking.menu_items.add(MenuItem.objects.get(id=item_id))

        return redirect('index')
    else:
        items = MenuItem.objects.all()
        return render(request, 'catering/book.html', {'items': items})

def add_menu_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category = request.POST.get('category')

        MenuItem.objects.create(name=name, description=description, price=price, category=category)
        return redirect('menu')

    return render(request, 'catering/add_menu_item.html')
