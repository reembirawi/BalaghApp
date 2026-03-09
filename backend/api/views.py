from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import SuggestionSerializer, UserSerializer, ComplaintSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Complaint, Suggestion

class ComplaintListCreateView(generics.ListCreateAPIView):
    serializer_class = ComplaintSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        user = self.request.user        
        return Complaint.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ComplaintDestroyView(generics.DestroyAPIView):
    serializer_class = ComplaintSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user        
        return Complaint.objects.filter(owner=user)

class SuggestionListCreateView(generics.ListCreateAPIView):
    serializer_class = SuggestionSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        user = self.request.user        
        return Suggestion.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SuggestionDestroyView(generics.DestroyAPIView):
    serializer_class = SuggestionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user        
        return Suggestion.objects.filter(owner=user)

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
