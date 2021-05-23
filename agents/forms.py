from leads.models import Agent
from django import forms


class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = [
            'user',
            ]
