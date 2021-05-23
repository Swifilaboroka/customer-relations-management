from .views import LeadCreateView, LeadDeleteView, LeadListView, LeadUpdateView, landing, lead_create, lead_detail, lead_list, lead_update
from django.urls import path

app_name = 'leads'

urlpatterns = [
    path('', landing, name='landing-page'),
    # path('list/', lead_list, name='lead-list'),
    # path('create/', lead_create, name='lead-create'),
    # path('update/<int:pk>/', lead_update, name='lead-update'),
    path('detail/<int:pk>/', lead_detail, name='lead-detail'),
    path('update/<int:pk>/', LeadUpdateView.as_view(), name='lead-update'),
    path('list/', LeadListView.as_view(), name='lead-list'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
    path('delete/<int:pk>/', LeadDeleteView.as_view(), name='lead-delete'),
]
