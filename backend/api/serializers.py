from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Complaint, Suggestion


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user
    
class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'owner', 'status']
        read_only_fields = ['id', 'created_at', 'updated_at', 'owner']

class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'owner', 'status']
        read_only_fields = ['id', 'created_at', 'updated_at', 'owner']
        