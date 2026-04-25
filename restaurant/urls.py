from django.contrib import admin
from django.urls import path
from .views import sayHello, index, MenuItemView, SingleMenuItemView, BookingViewSet, msg

urlpatterns = [
    path('menu/', MenuItemView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    path('booking/table/', BookingViewSet.as_view({'get': 'list'})),
    path('message/', msg),
    path('sayHello', sayHello, name='sayHello'),
    path('', index, name='index'),
]