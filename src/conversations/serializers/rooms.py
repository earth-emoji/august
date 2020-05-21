from rest_framework import serializers

from conversations.models import Room

class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'