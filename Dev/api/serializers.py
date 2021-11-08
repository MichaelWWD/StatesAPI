from states.models import States
from rest_framework import serializers

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = '__all__'
