from users.models import CustomUser
from leads.models import Agent
from django import forms


class AgentModelForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'email',
            ]
