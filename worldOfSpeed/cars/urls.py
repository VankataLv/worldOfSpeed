from django.urls import path, include

from worldOfSpeed.cars.views import show_catalogue, create_profile, car_details, car_edit, car_delete

urlpatterns = (
    path('catalogue/', show_catalogue, name='show-catalogue'),
    path('create/', create_profile, name='car-create'),
    path('<int:id>/', include([
        path('details/', car_details, name='car-details'),
        path('edit/', car_edit, name='car-edit'),
        path('delete/', car_delete, name='car-delete'),
    ]),
)
)