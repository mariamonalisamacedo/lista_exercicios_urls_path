from django.urls import path
from . import views

urlpatterns = [
    path('categoria/<str:categoria>/produto/<str:nome>/', views.produto, name='produto'),
]