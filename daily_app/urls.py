from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save_record/', views.save_record, name='save_record'),
    path('filterDate/', views.filterDate, name='filterDate'),
    # path('about/', views.about, name='about'),
]