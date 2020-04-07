from django.urls import path
from . import views

urlpatterns = [
    path('<str:email>/<str:testno>/<str:qno>/',views.exam,name='exam'),
]