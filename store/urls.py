from django.contrib import admin
from django.urls import path, include
from store.views import home, cart, orders, login, signout, signup

urlpatterns = [
    path('', home),
    path('cart/', cart),
    path('orders/', orders),
    path('login/', login),
    path('signup/', signup),
    path('logout/', signout),
    
]
