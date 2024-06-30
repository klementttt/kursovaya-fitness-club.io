# admin.py
from django.contrib import admin
from .models import Trainer, Subscription, Appointment, Cart

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'price', 'is_favorite', 'experience')  # Добавлено поле 'experience'
    search_fields = ('name', 'specialization')
    list_filter = ('is_favorite',)

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('trainer', 'user', 'date', 'time')
    search_fields = ('trainer__name', 'user__username')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)
