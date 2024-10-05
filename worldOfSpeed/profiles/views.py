from django.db.models import Sum
from django.shortcuts import render, redirect

from worldOfSpeed.cars.models import Car
from worldOfSpeed.profiles.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from worldOfSpeed.profiles.models import Profile


def create_profile(request):
    form = CreateProfileForm(request.POST or None)

    context = {
        'form': form,
    }

    if request.method == 'POST' and form.is_valid():
        form.save()

        return redirect('show-catalogue')

    return render(request, 'profile-create.html', context)


def view_profile(request):
    profile = Profile.objects.first()
    total_sum = Car.objects \
                    .filter(owner=profile, owner__isnull=False) \
                    .aggregate(total_price=Sum('price'))['total_price'] or 0
    context = {
        'profile': profile,
        'total_sum': total_sum,
    }

    return render(request, 'profile-details.html', context)


def edit_profile(request):
    profile = Profile.objects.first()
    form = EditProfileForm(instance=profile)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view-profile')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    form = DeleteProfileForm(instance=profile)

    if request.method == 'POST':
        profile.delete()
        return redirect('index')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profile-delete.html', context)


