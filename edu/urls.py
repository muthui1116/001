from django.urls import path
from . import views

urlpatterns = [
    path('post/<slug:slug>/', views.detail, name='post_detail'),
    path('search/', views.search, name='search'),
]
