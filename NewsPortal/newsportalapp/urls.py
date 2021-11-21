from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home_view,name='home'),
    path('cnews/',views.Cnews_view,name='cnews'),
    
]