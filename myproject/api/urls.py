from django.urls import path
from . import views

urlpatterns = [
    path('getTask/',views.getTask),
    path('addTask/', views.addTask),

    path('getUser/',views.getUser),
    path('addUser/', views.addUser),
]
