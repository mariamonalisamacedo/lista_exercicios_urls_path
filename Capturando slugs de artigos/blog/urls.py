from django.urls import path
from . import views

urlpatterns = [
    path('artigo/<slug:slug>/', views.artigo, name='artigo'),
]
