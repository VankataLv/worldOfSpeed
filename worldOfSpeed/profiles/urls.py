from django.urls import path

from worldOfSpeed.profiles.views import create_profile, view_profile, edit_profile, delete_profile

urlpatterns = (
    path('create/', create_profile, name='create-profile'),
    path('details/', view_profile, name='view-profile'),
    path('edit/', edit_profile, name='edit-profile'),
    path('delete/', delete_profile, name='delete-profile'),
)


