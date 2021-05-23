from .views import AgentCreateView, AgentDeleteView, AgentDetailView, AgentListView, AgentUpdateView
from django.urls import path

app_name = 'agents'

urlpatterns = [
    # path('list/', lead_list, name='lead-list'),
    # path('create/', lead_create, name='lead-create'),
    # path('update/<int:pk>/', lead_update, name='lead-update'),
    path('list/', AgentListView.as_view(), name='agent-list'),
    path('create/', AgentCreateView.as_view(), name='agent-create'),
    path('detail/<int:pk>/', AgentDetailView, name='agent-detail'),
    path('update/<int:pk>/', AgentUpdateView.as_view(), name='agent-update'),
    path('delete/<int:pk>/', AgentDeleteView.as_view(), name='agent-delete'),
]
