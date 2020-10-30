
from django.urls import path,include
from FirstPage import views

urlpatterns = [
    path('',views.home,name='home'),
    # path('home',views.home,name='home'),
    path('services',views.services,name='services'),
    path('Contact',views.contact,name='Contact')
]