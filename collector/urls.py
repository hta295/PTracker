from django.urls import path

from . import views

app_name = 'collector'
urlpatterns = [
    path('', views.index, name='index'),
]