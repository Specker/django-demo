"""DjangoDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from Views.views import mainpage_view
from Parking.views import parking_detail_view
from Car.views import car_detail_view, car_drive_view
from Registration.views import register_view

urlpatterns = [
    path('admin/', admin.site.urls, name='home'),
    path('', mainpage_view),
    path('Home/', mainpage_view),
    path('Parking/', parking_detail_view),
    path('Car/', car_detail_view),
    path('Car/Drive/<int:car_id>/', car_drive_view),
    path('', include('django.contrib.auth.urls')),
    path('Registration/', register_view),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
