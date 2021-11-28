from django.urls import path
from django.views.generic.list import ListView

from leads.models import Lead
from .views import LeadListView, LeadCreateView, lead_delete, LeadDetailView, LeadUpdateView

app_name = "leads"
urlpatterns = [
    path('', LeadListView.as_view(), name="lead_list"),
    path('<int:pk>/', LeadDetailView.as_view(), name="lead_details"),
    path('create/', LeadCreateView.as_view(), name="lead_create"),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name="lead_update"),
    path('<int:pk>/delete/', lead_delete, name="lead_delete"),
]
