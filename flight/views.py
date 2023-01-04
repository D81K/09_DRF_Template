from django.shortcuts import render
from .serializers import FlightSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Flight


# Create your views here.

class FlightViewSet(ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
