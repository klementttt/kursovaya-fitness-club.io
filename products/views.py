# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from .models import Trainer, Subscription, Appointment, Cart, Booking
from .forms import AppointmentForm, BookingForm
import json
from datetime import date, datetime

def home(request):
    best_trainers = Trainer.objects.filter(is_best=True)
    return render(request, 'products/home.html', {'best_trainers': best_trainers})

def about(request):
    favorit_trainers = Trainer.objects.filter(is_favorite=True)
    return render(request, 'products/about.html', {'favorit_trainers': favorit_trainers})

def where_to_find_us(request):
    return render(request, 'products/where_to_find_us.html', {})

def checkout(request):
    return render(request, 'products/checkout.html')

def product_detail(request, pk):
    product = get_object_or_404(Subscription, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

def catalog(request):
    subscriptions = Subscription.objects.all()
    trainers = Trainer.objects.all()
    return render(request, 'products/catalog.html', {'subscriptions': subscriptions, 'trainers': trainers})

def subscription_list(request):
    subscriptions = Subscription.objects.all()
    return render(request, 'products/subscription_list.html', {'subscriptions': subscriptions})

def buy_subscription(request, subscription_id):
    subscription = get_object_or_404(Subscription, pk=subscription_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.subscriptions.add(subscription)
    return redirect('cart')

def subscription_detail_view(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    return render(request, 'products/subscription_detail.html', {'subscription': subscription})

def trainer_detail_view(request, pk):
    trainer = get_object_or_404(Trainer, pk=pk)
    return redirect('book_trainer', trainer_id=pk)

@login_required
def profile(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'products/profile.html', {'appointments': appointments})

@login_required
def cart_view(request):
    cart = Cart.objects.get(user=request.user)  
    subscriptions = cart.subscriptions.all()
    bookings = cart.bookings.all()
    total_price = sum(item.price for item in subscriptions) + sum(item.trainer.price for item in bookings)
    
    context = {
        'subscriptions': subscriptions,
        'bookings': bookings,
        'total_price': total_price,
    }
    return render(request, 'products/cart.html', context)

@login_required
def remove_booking_from_cart(request, booking_id):
    cart = Cart.objects.get(user=request.user)
    booking = get_object_or_404(Booking, pk=booking_id)
    cart.bookings.remove(booking)
    booking.delete()
    return redirect('cart')

@login_required
def remove_from_cart(request, subscription_id):
    cart = Cart.objects.get(user=request.user)
    subscription = get_object_or_404(Subscription, pk=subscription_id)
    cart.subscriptions.remove(subscription)
    return redirect('cart')

def add_to_cart(request, subscription_id):
    subscription = get_object_or_404(Subscription, pk=subscription_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.subscriptions.add(subscription)
    return redirect('catalog')

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (date, datetime)):
            return obj.isoformat()
        return super().default(obj)

logout_view = LogoutView.as_view(next_page='/')

@login_required
def book_trainer(request, trainer_id):
    trainer = get_object_or_404(Trainer, pk=trainer_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.trainer = trainer
            booking.save()
            cart, created = Cart.objects.get_or_create(user=request.user)
            cart.bookings.add(booking)
            return redirect('cart')
    else:
        form = BookingForm()
    return render(request, 'products/book_trainer.html', {'form': form, 'trainer': trainer})

def callback_request(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        # Логика для обработки данных формы, например, сохранение в базу данных
        print(f"Получен запрос на обратный звонок от {name} с номером {phone}")
        return redirect('home')
    return render(request, 'products/callback_request.html')
