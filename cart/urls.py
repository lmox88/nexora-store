from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_detail, name='cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('decrease/<int:product_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('update/<int:product_id>/', views.update_cart, name='update_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path(
    'create-checkout-session/',
    views.create_checkout_session,
    name='create_checkout_session'
    ),

    path(
        'payment-success/',
        views.payment_success,
        name='payment_success'
    ),
]