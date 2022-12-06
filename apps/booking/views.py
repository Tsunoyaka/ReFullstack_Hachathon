from rest_framework import status
from rest_framework.viewsets import ModelViewSet 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from collections import namedtuple
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Booking
from apps.room.models import RoomNum
from .serializers import BookingSerializer

class BookingView(CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    # permission_classes = [IsAdminUser, IsAuthenticated]


class BookingListView(ListAPIView):
    queryset = RoomNum.objects.filter(is_booked='False')
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context