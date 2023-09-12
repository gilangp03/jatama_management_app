from django.urls import path
from main.views import show_main
from main.views import show_inventory

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('main/', show_main, name='show_main'),
    path('inventory/', show_inventory, name='show_inventory'),
]