from django.urls import path
from .views import  helloPageView

urlpatterns = [
    path('',helloPageView)
]