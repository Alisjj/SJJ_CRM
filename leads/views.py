from django.db.models import query
from django.shortcuts import render, render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from agents.mixins import OrganizerAndLoginRequiredMixin
from .models import Lead, Category
from .forms import AssignAgentForm, CustomerUserCreation, LeadModelForm, LeadCategoryUpdateForm

from django.views import generic


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomerUserCreation

    def get_success_url(self):
        return reverse("login")


class LandinPageView(generic.TemplateView):
    template_name = "landing.html"


class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/lead_list.html"
    context_object_name = "leads"

    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(
                organization=user.userprofile, agent__isnull=False)
        else:
            queryset = Lead.objects.filter(
                organization=user.agent.organization, agent__isnull=False)
            # filtered Leads for the Agent
            queryset = queryset.filter(agent__user=user)
        return queryset

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(LeadListView, self).get_context_data(**kwargs)
        if user.is_organizer:
            queryset = Lead.objects.filter(
                organization=user.userprofile, agent__isnull=True)
            context.update({
                "unassigned_leads": queryset
            })
        return context


class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "leads/lead_detail.html"
    context_object_name = "lead"

    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = Lead.objects.filter(
                organization=user.agent.organization)
            # filtered Leads for the Agent
            queryset = queryset.filter(agent__user=user)
        return queryset


class LeadCreateView(OrganizerAndLoginRequiredMixin, generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_form_kwargs(self, **kwargs):
        kwargs = super(LeadCreateView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            "request": self.request
        })
        return kwargs

    def get_success_url(self):
        return reverse("leads:lead_list")

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organization = self.request.user.userprofile
        agent.save()
        send_mail(
            subject="A lead has been created.", message="Goto the Web site and attend to your lead",
            from_email="test@test.com", recipient_list=["test2@test.com"]
        )
        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(OrganizerAndLoginRequiredMixin, generic.UpdateView):
    # queryset = Lead.objects.all()
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm

    def get_form_kwargs(self, **kwargs):
        kwargs = super(LeadUpdateView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            "request": self.request
        })
        return kwargs

    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organization=user.userprofile)

    def get_success_url(self):
        return reverse("leads:lead_details", kwargs={"pk": self.get_object().id})


class LeadDeleteView(OrganizerAndLoginRequiredMixin, generic.DeleteView):
    template_name = "leads/lead_delete.html"

    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organization=user.userprofile)

    def get_success_url(self):
        return reverse("leads:lead_list")


class AssignAgentView(OrganizerAndLoginRequiredMixin, generic.FormView):
    template_name = "leads/assign_agent.html"
    form_class = AssignAgentForm

    def get_form_kwargs(self, **kwargs):
        kwargs = super(AssignAgentView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            "request": self.request
        })
        return kwargs

    def get_success_url(self):
        return reverse("leads:lead_list")

    def form_valid(self, form):
        agent = form.cleaned_data["agent"]
        lead = Lead.objects.get(id=self.kwargs["pk"])
        lead.agent = agent
        lead.save()
        return super(AssignAgentView, self).form_valid(form)


class CategoryListView(OrganizerAndLoginRequiredMixin, generic.ListView):
    model = Category
    template_name = "leads/category_list.html"
    context_object_name = "category_list"

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        user = self.request.user

        if user.is_organizer:
            queryset = Lead.objects.filter(
                organization=user.userprofile, )
        else:
            queryset = Lead.objects.filter(
                organization=user.agent.organization)

        context.update({
            "unassigned_lead_count": queryset.filter(category__isnull=True).count()
        })
        return context

    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Category.objects.filter(
                organization=user.userprofile, )
        else:
            queryset = Category.objects.filter(
                organization=user.agent.organization)
        return queryset


class CategoryDetailView(OrganizerAndLoginRequiredMixin, generic.DetailView):
    model = Category
    template_name = "leads/category_detail.html"
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        leads = self.get_object().leads.all()
        context.update({
            "leads": leads
        })
        return context

    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Category.objects.filter(
                organization=user.userprofile, )
        else:
            queryset = Category.objects.filter(
                organization=user.agent.organization)
        return queryset


class LeadCategoryUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "leads/lead_category_update.html"
    form_class = LeadCategoryUpdateForm

    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = Lead.objects.filter(
                organization=user.agent.organization)
            # filtered Leads for the Agent
            queryset = queryset.filter(agent__user=user)
        return queryset

    def get_success_url(self):
        return reverse("leads:lead_details", kwargs={"pk": self.get_object().id})
