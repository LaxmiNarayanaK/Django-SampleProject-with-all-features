from rest_framework import serializers
from .models import Destination
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Destination.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
class DestinationSerializer(serializers.ModelSerializer):

    class Meta:
        model=Destination
        fields="__all__"

