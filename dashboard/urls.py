from django.urls import path
from . import views

urlpatterns = [
    path('<str:email>/',views.profile,name='profile'),
]