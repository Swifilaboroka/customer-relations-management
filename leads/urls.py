from .views import LeadCreateView, LeadDeleteView, LeadDetailView, LeadListView, LeadUpdateView, landing
from django.urls import path

app_name = 'leads'

urlpatterns = [
    path('', landing, name='landing-page'),
    path('detail/<int:pk>/', LeadDetailView, name='lead-detail'),
    path('update/<int:pk>/', LeadUpdateView.as_view(), name='lead-update'),
    path('list/', LeadListView.as_view(), name='lead-list'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
    path('delete/<int:pk>/', LeadDeleteView.as_view(), name='lead-delete'),
]
