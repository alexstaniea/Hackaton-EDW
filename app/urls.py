from django.urls import path
from . import views

from app.views import (

    RegisterView,
    LoginView,
    LogoutView,
    UserProfileView,
    UserProfileUpdateView,
    CartDetailView,
    cart_checkout,
    UserProfileUpdateView,
    index,
    article_detail,
    ReviewCreateView,
    index_review,
    add_to_cart,
    remove_from_cart,
    article_detail,
    ReviewCreateView,
    ReviewDeleteView
)

urlpatterns = [
    path('', index, name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('userprofile/<int:pk>', UserProfileView.as_view(), name='user_profile'),
    path('userprofile/<int:pk>/edit', UserProfileUpdateView.as_view(), name='user_profile_edit'),
    path('article/<int:pk>', article_detail, name='article_detail'),
    path('article/<int:pk>/review/create', ReviewCreateView.as_view(), name='review_create'),
    path('article/<int:article_pk>/review/delete/<int:pk>', ReviewDeleteView.as_view(), name='review_delete'),
    path('cart/<int:pk>', CartDetailView.as_view(), name='cart_detail'),
    path('cart_checkout/<int:pk>', cart_checkout, name='cart_checkout'),
    path('article/<int:pk>/add', add_to_cart, name='add_to_cart'),
    path('article/<int:pk>/remove', remove_from_cart, name='remove_from_cart'),
    path('article/<int:pk>/index_review', index_review, name='index_review'),
]


