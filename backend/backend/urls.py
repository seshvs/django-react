
# backend/urls.py

from django.contrib import admin
from django.urls import path, include                 # add this

urlpatterns = [
    path('admin/', admin.site.urls),           
    path('kogan/', include('kogan.urls'))
]
