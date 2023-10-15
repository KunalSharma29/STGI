from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name = 'Home'),
    path('results', views.results, name = 'results'),
    path('mean', views.mean, name = 'mean'),
    path('median', views.median, name = 'median'),
    path('salary25', views.salary25, name = 'salary25'),
    path('salary75', views.salary75, name = 'salary75' )
    
] 