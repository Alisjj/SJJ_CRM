from django.conf import settings
from leads.views import SignupView
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from leads.views import LandinPageView

urlpatterns = [
    path('', LandinPageView.as_view(), name="landing"),
    path('admin/', admin.site.urls),
    path('agents/', include('agent.urls', namespace="agents")),
    path('leads/', include('leads.urls', namespace="leads")),
    path('signup/', SignupView.as_view(), name="signup"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
