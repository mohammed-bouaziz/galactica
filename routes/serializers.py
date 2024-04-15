from rest_framework import serializers
from .models import Routes

class RoouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routes
        fields = ['origin', 'destination', 'travel_time']

        