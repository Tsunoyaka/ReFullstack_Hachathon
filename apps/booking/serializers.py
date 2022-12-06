from rest_framework import serializers

from apps.account.models import User
from apps.hotel.serializers import HotelSerializer
from apps.room.serializers import RoomSerializer
from .models import Booking 


class GuestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = User
        fields = ("user", "email")
        

class BookingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        default=serializers.CurrentUserDefault(),
        source='user.username'
    )

    def validate(self, attrs):
        user = self.context['request'].user
        attrs['user'] = user
        return attrs
        
    class Meta:
        model = Booking
        fields =("user", "hotel", "room", "checkin_date", "checkout_date", 'charge')