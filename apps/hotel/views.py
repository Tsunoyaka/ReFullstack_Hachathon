from urllib.request import Request
from django_filters import rest_framework as rest_filter
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema

from .serializers import HotelListSerializer, HotelCreateSerializer, HotelSerializer, HotelUpdateSerializer
from .models import Hotel
from .permissions import IsOwner

from rest_framework.views import APIView

class PriceFilter(rest_filter.FilterSet):
    max_price = rest_filter.NumberFilter(field_name="room_manager__room_price", lookup_expr='lt')
    min_price = rest_filter.NumberFilter(field_name="room_manager__room_price", lookup_expr='gt')

    class Meta:
        model = Hotel
        fields = ['region', 'stars']



class HotelListViewSet(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer
    filter_backends = [
        filters.SearchFilter, 
        rest_filter.DjangoFilterBackend, 
        filters.OrderingFilter]
    search_fields = ['title','stars']
    filterset_fields = ['pets', 'food', 'region']
    ordering_fields = ['room_manager__room_price']
    range_fields = ['room_manager__room_price']
    filterset_class = PriceFilter

    def partial_update(self, request, pk):
        try:
            instance = Hotel.objects.get(pk=pk)
            serailizer = HotelCreateSerializer(data=request.data, instance=instance, context={'request': request})
            if serailizer.is_valid(raise_exception=True):            
                serailizer.save()  
            return Response('Отель успешно изменен')
        except Hotel.DoesNotExist:
            return Response('Страница не найдена!', status=status.HTTP_404_NOT_FOUND)


    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
        
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return HotelListSerializer
        elif self.action == 'create':
            return HotelCreateSerializer
        elif self.action == 'retrieve':
            return HotelSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['create']:
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        if self.action in ['destroy', 'update', 'partial_update']:
            self.permission_classes = [IsOwner]
        return super().get_permissions()


@swagger_auto_schema(HotelUpdateSerializer)
class UpdHotelView(APIView):
    permission_classes = [IsAdminUser, IsOwner]
    
    def put(self, request, pk):
        # print(pk, type(pk))
        obj = Hotel.objects.get(slug=pk)
        serializer = HotelUpdateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.update(obj, serializer.validated_data)
            answer = {"status": "UPDATE" }
            answer.update(serializer.data)
            return Response(answer)

