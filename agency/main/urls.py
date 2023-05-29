from django.urls import path
from .views import *


app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('filtered/', filtered_real_estate, name='filtered'),
    path('owner/', user_get_owner_status, name='stay_owner'),
    path('estate_detail/<int:estate_id>/', estate_detail, name='detail'),
    path('add_new_estate/', add_new_estate, name='add_estate'),
    path('discounts_list/', discount_list, name='discount'),
    path('realtors_list/', realtor_list, name='realtor')
]