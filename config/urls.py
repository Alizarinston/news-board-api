from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView


urlpatterns = [
    path("", RedirectView.as_view(url="/api/")),
    path("api/", include("posts.urls")),
    path("api/auth/", include("auth_api.urls")),
    path("admin/", admin.site.urls),
]
