from django.urls.base import reverse
from django.views.generic.edit import DeleteView, UpdateView
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentForm


class AgentListView(LoginRequiredMixin, ListView):
    template_name = 'agents/agent_list.html'
    context_object_name = 'agents'

    def get_queryset(self):
        return Agent.objects.all()


class AgentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentForm

    def get_success_url(self) -> str:
        return reverse('agents:agent-list')

    def form_valid(self, form):
        form.instance.organization = self.request.user.user_profile
        return super().form_valid(form)


def agent_detail(request, pk):
    agent = get_object_or_404(Agent, pk=pk)
    return render(request=request, template_name='agents/agent_detail.html', context={"agent": agent})

class AgentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'agents/agent_update.html'
    form_class = AgentForm
    queryset = Agent.objects.all()

    def get_success_url(self) -> str:
        return reverse('agents:agent-list')

class AgentDeleteView(LoginRequiredMixin, DeleteView):
    queryset = Agent.objects.all()
    template_name = 'agents/agent_delete.html'

    def get_success_url(self) -> str:
        return reverse('agents:agent-list')
