from django.urls import path
from .views import card_add, cart_detail, cart_remove

app_name = 'cart'

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', card_add, name='cart_add'),
    path('remove/<int:product_id>/', cart_remove, name='cart_remove')
]