from rest_framework import serializers
from .models import Flight, Reservation, Passenger


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    passenger = PassengerSerializer(many=True)
    flight = serializers.StringRelatedField()
    user = serializers.StringRelatedField()
    class Meta:
        model = Reservation
        fields = '__all__'