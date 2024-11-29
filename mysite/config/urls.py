from django.contrib import admin
from django.urls import path, include

from pybo2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo2/', include('pybo2.urls')),
]


