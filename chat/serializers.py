from rest_framework import serializers
from .models import Chat

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "room_name",
            "users",
        )
        model = Chat

