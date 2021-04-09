from django.urls import path
from profiles_api import views

urlaptterns=[
    path('hello-view/', views.HelloAPIView.as_view()),

]
