from django.urls import path

from app1 import views

urlpatterns = [
    path('signup/',views.signup),
    path('login/',views.login_page),
    path('home/',views.home)
]
