from django.urls import path
from . import views
urlpatterns = [
    path('complaints/', views.ComplaintListCreateView.as_view(), name='complaint-list-create'),
    path('complaints/delete/<int:pk>/', views.ComplaintDestroyView.as_view(), name='complaint-destroy'),
    path('suggestions/', views.SuggestionListCreateView.as_view(), name='suggestion-list-create'),
    path('suggestions/delete/<int:pk>/', views.SuggestionDestroyView.as_view(), name='suggestion-destroy'),
]