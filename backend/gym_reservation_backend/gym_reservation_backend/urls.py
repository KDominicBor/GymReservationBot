"""
URL configuration for gym_reservation_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# reservation_app/urls.py

from django.urls import include, path
from reservation_app.views import reserve_gym_slot
from django.contrib import admin
from reservation_app import urls as reservation_app_urls



urlpatterns = [
    path('reserve/', reserve_gym_slot, name='reserve_gym_slot'),
    path('admin/', admin.site.urls),
    path('api/', include('reservation_app.urls')),
    path('api/', include(reservation_app_urls)),
]



