from django.urls.base import reverse
from users.models import CustomUser
from users.forms import CustomUserCreationForm
from django.views.generic.edit import CreateView


# Create your views here.
class SignUpView(CreateView):
    model = CustomUser
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self) -> str:
        return reverse('users:login')

