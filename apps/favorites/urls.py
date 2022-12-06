from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static

from .views import FavoritesView, MyFavoritesView




urlpatterns = [
    path('add-favorite/', FavoritesView.as_view()),
    path('my-favorites', FavoritesView.as_view()),
]
