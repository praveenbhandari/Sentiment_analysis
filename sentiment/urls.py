from django.urls import path
from . import views

urlpatterns=[
    path("", views.home, name="home"),   
    path("index", views.index, name="index"),
    path('',views.home,name='home'),
    path('test-input',views.testInput, name="test-input"),
    path('result',views.grid,name='result'),
    path('result1',views.ridge,name='result1')
]