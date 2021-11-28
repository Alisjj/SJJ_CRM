from django.contrib import admin
from django.urls import path, include
from leads.views import LandinPageView

urlpatterns = [
    path('', LandinPageView.as_view(), name="landing"),
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls', namespace="leads")),
]
