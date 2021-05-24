from agents.mixins import OrganizerAndLoginRequiredMixin
from django.urls.base import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent, Lead
from leads.forms import LeadForm


def landing(request):
    return render(request, 'landing.html')

class LeadDetailView(LoginRequiredMixin, DetailView):
    queryset = Lead.objects.all()
    template_name = 'leads/lead_detail.html'

class LeadListView(LoginRequiredMixin, ListView):
    context_object_name = 'leads'

    def get_queryset(self):
        queryset = Lead.objects.all()
        user = self.request.user
        if user.is_organizer:
            queryset = queryset.filter(organization_id=user.user_profile.id)
        elif user.is_agent:
            queryset = queryset.filter(organization_id=user.agent.organization.id)
            queryset = queryset.filter(agent__user_id=user.id)
            return queryset
        return queryset


class LeadCreateView(OrganizerAndLoginRequiredMixin, CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadForm

    def get_success_url(self) -> str:
        return reverse('leads:lead-list')


class LeadUpdateView(OrganizerAndLoginRequiredMixin, UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadForm
    queryset = Lead.objects.all()

    def get_queryset(self):
        user = self.request.user
        queryset = Lead.objects.filter(organization_id=user.user_profile.id)
        return queryset

    def get_success_url(self) -> str:
        return reverse('leads:lead-list')

class LeadDeleteView(OrganizerAndLoginRequiredMixin, DeleteView):
    template_name = 'leads/lead_delete.html'

    def get_queryset(self):
        queryset = Lead.objects.all()
        user = self.request.user
        if user.is_organizer:
            queryset = queryset.filter(organization_id=user.user_profile.id)
        elif user.is_agent:
            queryset = queryset.filter(organization_id=user.agent.organization.id)
            queryset = queryset.filter(agent__user_id=user.id)
            return queryset
        return queryset

    def get_success_url(self) -> str:
        return reverse('leads:lead-list')
