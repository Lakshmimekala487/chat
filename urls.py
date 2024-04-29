from django.urls import path
from.import views
from django.contrib.auth import views as auth_views





urlpatterns = [
    # urls.py
    # Other URL patterns
    # path('home/',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/',views.signupPage,name='signupurl'),
    path('register/',views.register,name="registerurl"),
    path('Forgetpassword/',views.Forgetpassword,name='Forgetpasswordurl'),
    path("", views.rooms, name="rooms"),
    path("<str:slug>", views.room, name="room"),
]