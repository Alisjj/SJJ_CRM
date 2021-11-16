from django.urls import path
from . import views

app_name = "leads"
urlpatterns = [
    path('', views.lead_list, name="lead_list"),
    path('<int:pk>/', views.lead_detail, name="lead_details"),
    path('create/', views.lead_create, name="lead_create"),
    path('<int:pk>/update/', views.lead_update, name="lead_update"),
    path('<int:pk>/delete/', views.lead_delete, name="lead_delete"),
]
