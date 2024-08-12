from django.contrib import admin
from django.urls import include, path
from core.urls import *
from core.views import *

urlpatterns = [
    path("core/", include("core.urls")),
    path("admin/", admin.site.urls),
    path("",views.landing, name="landing"),
]