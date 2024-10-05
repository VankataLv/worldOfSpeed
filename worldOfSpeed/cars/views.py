from django.shortcuts import render, redirect, get_object_or_404

from worldOfSpeed.cars.forms import CarCreateForm, CarEditForm, CarDeleteForm
from worldOfSpeed.cars.models import Car
from worldOfSpeed.profiles.models import Profile


def show_catalogue(request):
    user = Profile.objects.first()
    listed_cars = Car.objects.all().order_by('pk')
    cars_count = len(listed_cars)
    context = {
        'user': user,
        'listed_cars': listed_cars,
        'cars_count': cars_count,
    }

    return render(request, 'catalogue.html', context)


def create_profile(request):
    form = CarCreateForm(request.POST or None)
    user = Profile.objects.first()

    if request.method == 'POST' and form.is_valid():
        form.instance.owner_id = user.pk
        form.save()
        return redirect('show-catalogue')

    context = {'form': form,}
    return render(request, 'car-create.html', context)


def car_details(request, id:int):
    selected_car = Car.objects.get(pk=id)
    context = {
        'selected_car': selected_car,
    }
    return render(request, 'car-details.html', context)


def car_edit(request, id:int):
    selected_car = get_object_or_404(Car, pk=id)

    if request.method == 'POST':
        form = CarEditForm(request.POST, instance=selected_car)
        if form.is_valid():
            form.save()
            return redirect('show-catalogue')

    form = CarEditForm(instance=selected_car)
    context = {
        'car': selected_car,
        'form': form,
    }

    return render(request, 'car-edit.html', context)


def car_delete(request, id:int):
    selected_car = get_object_or_404(Car, pk=id)

    if request.method == 'POST':
        selected_car.delete()
        return redirect('show-catalogue')

    form = CarDeleteForm(instance=selected_car)
    context = {
        'car': selected_car,
        'form': form,
    }
    return render(request, 'car-delete.html', context)