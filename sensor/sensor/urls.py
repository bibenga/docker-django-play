from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('api/admin/', admin.site.urls),
]
