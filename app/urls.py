from django.urls import path

from app.views import (

    RegisterView,
    LoginView,
    LogoutView,
    UserProfileView,
    UserProfileUpdateView,
    CartDetailView,
    cart_checkout
)

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('userprofile/<int:pk>', UserProfileView.as_view(), name='user_profile'),
    path('userprofile/<int:pk>/edit', UserProfileUpdateView.as_view(), name='user_profile_edit'),
    path('cart/<int:pk>', CartDetailView.as_view(), name='cart_detail'),
    path('cart_checkout/<int:pk>', cart_checkout, name='cart_checkout')
]