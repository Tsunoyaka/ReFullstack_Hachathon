# from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import BookingView, BookingListView


urlpatterns = [
  # re_path(r"^(?P<api_name>[a-z]+)", ListView, name='booking'),
  path('reservation/', BookingView.as_view()),
  path('list_reservation/', BookingListView.as_view())
]
# router = DefaultRouter()
# router.register('bookings', ListView, 'booking')

# urlpatterns = [

# ]

# urlpatterns += router.urls