from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products import views as product_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_views.home, name='home'),
    path('about/', product_views.about, name='about'),
    path('catalog/', product_views.catalog, name='catalog'),
    path('profile/', product_views.profile, name='profile'),
    path('where_to_find_us/', product_views.where_to_find_us, name='where_to_find_us'),
    path('trainer/<int:pk>/', product_views.trainer_detail_view, name='trainer_detail'),
    path('trainer/<int:trainer_id>/book/', product_views.book_trainer, name='book_trainer'),
    path('subscription/<int:pk>/', product_views.subscription_detail_view, name='subscription_detail'),
    path('cart/', product_views.cart_view, name='cart'),
    path('checkout/', product_views.checkout, name='checkout'),
    path('add_to_cart/<int:subscription_id>/', product_views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:subscription_id>/', product_views.remove_from_cart, name='remove_from_cart'),
    path('remove_booking_from_cart/<int:booking_id>/', product_views.remove_booking_from_cart, name='remove_booking_from_cart'),  # Добавьте эту строку
    path('users/', include('users.urls')),
    path('logout/', product_views.logout_view, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
