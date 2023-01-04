from django.shortcuts import render
from .serializers import FlightSerializer, ReservationSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Flight, Reservation
from .permissions import IsAdminOrReadOnly


# Create your views here.

class FlightViewSet(ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAdminOrReadOnly]


class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer