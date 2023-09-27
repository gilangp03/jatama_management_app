from django.urls import path
from main.views import show_main, show_inventory, add_inventory, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user


urlpatterns = [
    path('', show_main, name='show_main'),
    path('inventory/', show_inventory, name='show_inventory'),
    path('add-inventory/', add_inventory, name='add_inventory'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]