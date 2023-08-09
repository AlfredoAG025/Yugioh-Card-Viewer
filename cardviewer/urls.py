from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_card_back, name='card_back'),
    path('show_card/', views.show_card, name='show_card'),
]