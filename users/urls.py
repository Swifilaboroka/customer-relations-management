from users.views import SignUpView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls.conf import path

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    # path('update/<int:pk>/', LeadUpdateView.as_view(), name='lead-update'),
    # path('list/', LeadListView.as_view(), name='lead-list'),
    # path('create/', LeadCreateView.as_view(), name='lead-create'),
    # path('delete/<int:pk>/', LeadDeleteView.as_view(), name='lead-delete'),
]
