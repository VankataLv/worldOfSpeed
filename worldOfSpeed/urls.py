from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('worldOfSpeed.common.urls')),
    path('cars/', include('worldOfSpeed.cars.urls')),
    path('profile/', include('worldOfSpeed.profiles.urls')),
]
