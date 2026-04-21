from django.contrib import admin
from django.urls import path
from .views import sayHello, index

urlpatterns = [
    path('sayHello', sayHello, name='sayHello'),
    path('', index, name='index'),
]