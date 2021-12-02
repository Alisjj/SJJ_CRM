from django.shortcuts import render, render, reverse
from django.core.mail import send_mail
# from django.http import HttpResponse
from .models import Lead
from .forms import CustomerUserCreation, LeadModelForm
# from django.views.generic import TemplateView
# Create your views here.

from django.views import generic
from leads import models


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomerUserCreation

    def get_success_url(self):
        return reverse("login")


class LandinPageView(generic.TemplateView):
    template_name = "landing.html"


class LeadListView(generic.ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


class LeadDetailView(generic.DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


class LeadCreateView(generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead_list")

    def form_valid(self, form):
        send_mail(
            subject="A lead has been created.", message="Goto the Web site and attend to your lead",
            from_email="test@test.com", recipient_list=["test2@test.com"]
        )
        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(generic.UpdateView):
    queryset = Lead.objects.all()
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead_detail")


class LeadDeleteView(generic.DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead_list")
