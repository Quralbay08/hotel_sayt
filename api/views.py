from django.shortcuts import render
from rest_framework.generics import ListAPIView,UpdateAPIView,CreateAPIView,RetrieveAPIView
from .serializers import HotelSerializer,CategorySerializer,RoomSerializer
from hotel.models import Hotel,Category,Room

# Create your views here.

class HotelView(ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    
    
class UpdateHotelView(UpdateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class CreateHotelView(CreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class RetrieveHotelView(RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer