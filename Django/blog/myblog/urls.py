from django.urls import path
from .views import show_home
from . import views

urlpatterns = [
    path('', show_home, name = 'home_url'),
]