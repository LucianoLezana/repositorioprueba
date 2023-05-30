from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_project_coder/', include('app_project_coder.urls')),
]
