from django.db.models import query
from django.shortcuts import render, render, reverse
from django.views.generic.edit import UpdateView
# from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadModelForm
from django.views.generic import TemplateView
# Create your views here.

from django.views.generic import TemplateView, ListView, DetailView, CreateView
from leads import models


class LandinPageView(TemplateView):
    template_name = "landing.html"


# def home(request):
#     return render(request, 'landing.html')

class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"

# def lead_list(request):
#     leads = Lead.objects.all()
#     context = {
#         'leads': leads
#     }
#     return render(request, "leads/lead_list.html", context)


class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


# def lead_detail(request, pk):
#     lead = Lead.objects.get(pk=pk)
#     context = {
#         'lead': lead
#     }
#     return render(request, "leads/lead_detail.html", context)

class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead_list")


# def lead_create(request):
#     form = LeadModelForm()
#     if request.method == "POST":
#         print("receiving Post request")
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return redirect("/leads")

#     context = {
#         "form": form
#     }
#     return render(request, "leads/lead_create.html", context)


# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm(instance=lead)
#     if request.method == "POST":
#         print("receiving Post request")
#         form = LeadModelForm(request.POST, instance=lead)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return redirect("/leads/")
#     context = {
#         "form": form,
#         "lead": lead,
#     }
#     return render(request, 'leads/lead_update.html', context)

class LeadUpdateView(UpdateView):
    queryset = Lead.objects.all()
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead_detail")


def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")
