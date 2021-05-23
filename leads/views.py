from django.urls.base import reverse
from django.views.generic.edit import DeleteView, UpdateView
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent, Lead
from leads.forms import LeadForm


def landing(request):
    return render(request, 'landing.html')

# Create your views here.
def lead_list(request):
    leads = Lead.objects.all()
    return render(request=request, template_name='leads/lead_list.html', context={'leads': leads})


def lead_detail(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    return render(request=request, template_name='leads/lead_detail.html', context={"lead": lead})


def lead_create(request):
    # GET
    form = LeadForm(request.POST)
    if form.is_valid():
        agent = Agent.objects.filter().first()
        agent_id = agent.id
        lead = Lead(agent_id=agent_id, **form.cleaned_data)
        lead.save()
        return redirect('/leads')
    return render(request, 'leads/lead_create.html', {'form': form})


def lead_update(request, pk):
    # GET
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == 'GET':
        form = LeadForm(instance=lead)
        return render(request, 'leads/lead_update.html', {'form': form, 'lead': lead})
    elif request.method == 'POST':
        form = LeadForm(instance=lead, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/leads')
        return render(request, 'leads/lead_update.html', {'form': form, 'lead': lead})


class LeadListView(LoginRequiredMixin, ListView):
    queryset = Lead.objects.all()
    context_object_name = 'leads'


class LeadCreateView(LoginRequiredMixin, CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadForm

    def get_success_url(self) -> str:
        return reverse('leads:lead-list')


class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadForm
    queryset = Lead.objects.all()

    def get_success_url(self) -> str:
        return reverse('leads:lead-list')

class LeadDeleteView(LoginRequiredMixin, DeleteView):
    queryset = Lead.objects.all()
    template_name = 'leads/lead_delete.html'

    def get_success_url(self) -> str:
        return reverse('leads:lead-list')
