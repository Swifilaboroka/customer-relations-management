from .views import landing, lead_create, lead_detail, lead_list, lead_update
from django.urls import path

app_name = 'leads'

urlpatterns = [
    path('', landing, name='landing-page'),
    path('create/', lead_create, name='lead-create'),
    path('detail/<int:pk>', lead_detail, name='lead-detail'),
    path('list/', lead_list, name='lead-list'),
    path('<int:pk>/update/', lead_update, name='update'),
]
