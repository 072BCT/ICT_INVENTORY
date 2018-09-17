from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('floor/<int:floor>', views.floor_view, name='floor_view'),
    path('room/<str:room>', views.room_view, name='room_view')
]
