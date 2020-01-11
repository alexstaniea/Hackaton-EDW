from django.urls import path

from app.views import (

    RegisterView,
    LoginView,
    LogoutView,
    UserProfileView,
    UserProfileUpdateView,
    index,
    article_detail,
    ReviewCreateView
)

from . import views

urlpatterns = [
    path('', index, name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('userprofile/<int:pk>', UserProfileView.as_view(), name='user_profile'),
    path('userprofile/<int:pk>/edit', UserProfileUpdateView.as_view(), name='user_profile_edit'),
    path('article/<int:pk>', article_detail, name='article_detail'),
    path('article/<int:pk>/review/create', ReviewCreateView.as_view(), name='review_create'),
]