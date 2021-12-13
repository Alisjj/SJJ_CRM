from django.urls import path
from django.views.generic.list import ListView

# from leads.models import Lead
from .views import LeadListView, LeadCreateView, LeadDetailView, LeadUpdateView, LeadDeleteView, AssignAgentView

app_name = "leads"
urlpatterns = [
    path('', LeadListView.as_view(), name="lead_list"),
    path('<int:pk>/', LeadDetailView.as_view(), name="lead_details"),
    path('create/', LeadCreateView.as_view(), name="lead_create"),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name="lead_update"),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name="lead_delete"),
    path('<int:pk>/assign-agent/', AssignAgentView.as_view(), name="assign_agent"),
]
