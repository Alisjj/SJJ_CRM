from django.urls import path

from leads.forms import LeadCategoryUpdateForm
# from leads.models import Lead
from .views import (
    LeadCategoryUpdateView, LeadListView, LeadCreateView, LeadDetailView,
    LeadUpdateView, LeadDeleteView, AssignAgentView, CategoryListView, CategoryDetailView
)

app_name = "leads"
urlpatterns = [
    path('', LeadListView.as_view(), name="lead_list"),
    path('<int:pk>/', LeadDetailView.as_view(), name="lead_details"),
    path('create/', LeadCreateView.as_view(), name="lead_create"),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name="lead_update"),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name="lead_delete"),
    path('<int:pk>/assign-agent/', AssignAgentView.as_view(), name="assign_agent"),
    path('categories/', CategoryListView.as_view(), name="category_list"),
    path('categories/<int:pk>/', CategoryDetailView.as_view(),
         name="category_details"),
    path('categories/<int:pk>/update/', LeadCategoryUpdateView.as_view(),
         name="category_update"),
]
