from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.
class LandingPageView(TemplateView):
    template_name = "leads/landing.html"


class LeadListView(ListView):
    template_name = "leads/list_leads.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


class LeadDetailView(DetailView):
    template_name = "leads/leads_details.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


class LeadCreateView(CreateView):
    template_name = "leads/leads_create.html"
    form_class = LeadModelForms

    def get_success_url(self):
        return reverse("leads:lead_list")


class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForms

    def get_success_url(self):
        return reverse("leads:lead_list")


def landing_page(request):
    return render(request, 'leads/landing.html')


def leads_list(request):
    leads = Lead.objects.all()
    context = {"leads": leads}
    return render(request, "leads/list_leads.html", context)
    # return HttpResponse('hello')


def leads_details(request, pk):
    lead = Lead.objects.get(id=pk)
    print(lead)
    context = {"lead": lead}
    return render(request, "leads/leads_details.html", context)


def leads_create(request):
    form = LeadModelForms()
    if request.method == "POST":
        form = LeadModelForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/leads')
    context = {
        "form": LeadModelForms()
    }
    return render(request, "leads/leads_create.html", context)




def lead_update(request, pk):
    lead = Lead.objects.get(pk=pk)
    form = LeadModelForms(instance=lead)
    if request.method == "POST":
        form = LeadModelForms(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form": form,
        "lead": lead
    }
    return render(request, 'leads/lead_update.html', context)


class LeadDeleteView(DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead_list")


def lead_delete(request, pk):
    lead = Lead.objects.get(pk=pk)
    lead.delete()
    return redirect("/leads")
