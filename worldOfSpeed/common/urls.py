from django.urls import path

from worldOfSpeed.common.views import index

urlpatterns = (
    path('', index, name='index'),
)
