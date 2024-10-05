from django.shortcuts import render

from worldOfSpeed.profiles.models import Profile


def index(request):
    profile = Profile.objects.first()

    context = {'user': profile}

    return render(request, 'index.html', context)
