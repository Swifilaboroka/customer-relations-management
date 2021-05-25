from django.shortcuts import redirect
from agents.mixins import OrganizerAndLoginRequiredMixin
from django.urls.base import reverse
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic import ListView, CreateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm


class AgentListView(OrganizerAndLoginRequiredMixin, ListView):
    template_name = 'agents/agent_list.html'
    context_object_name = 'agents'

    def get_queryset(self):
        organization = self.request.user.user_profile
        return Agent.objects.filter(organization=organization)


class AgentCreateView(OrganizerAndLoginRequiredMixin, CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentModelForm

    def get_success_url(self) -> str:
        return reverse('agents:agent-list')

    def form_valid(self, form):
        # form.instance.organization = self.request.user.user_profile
        user = form.instance
        user.is_agent = True
        user.is_organizer = False
        user.save()
        Agent.objects.create(user=user, organization=self.request.user.userprofile)
        return redirect('agents:agent-list')


class AgentDetailView(OrganizerAndLoginRequiredMixin, DetailView):
    template_name = 'agents/agent_detail.html'

    def get_queryset(self):
        organization = self.request.user.user_profile
        return Agent.objects.filter(organization=organization)

class AgentUpdateView(OrganizerAndLoginRequiredMixin, UpdateView):
    template_name = 'agents/agent_update.html'
    form_class = AgentModelForm
    queryset = Agent.objects.all()

    def get_queryset(self):
        organization = self.request.user.user_profile
        return Agent.objects.filter(organization=organization)

    def get_success_url(self) -> str:
        return reverse('agents:agent-list')

class AgentDeleteView(OrganizerAndLoginRequiredMixin, DeleteView):
    queryset = Agent.objects.all()
    template_name = 'agents/agent_delete.html'

    def get_queryset(self):
        organization = self.request.user.user_profile
        return Agent.objects.filter(organization=organization)

    def get_success_url(self) -> str:
        return reverse('agents:agent-list')
