from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from worldOfSpeed.cars.validators import validate_year_value
from worldOfSpeed.profiles.models import Profile


class Car(models.Model):
    TYPE_CHOICES = [
        ('rally', 'Rally'),
        ('open-wheel', 'Open-wheel'),
        ('kart', 'Kart'),
        ('drag', 'Drag'),
        ('other', 'Other'),
    ]
    MAX_LENGTH_TYPE = 10
    MAX_LENGTH_MODEL = 15
    MIN_LENGTH_MODEL = 1
    MIN_VALUE_PRICE = 1.0

    type = models.CharField(
                            choices=TYPE_CHOICES,
                            max_length=MAX_LENGTH_TYPE,
    )
    model = models.CharField(
                             blank=False, null=False,
                             max_length=MAX_LENGTH_MODEL,
                             validators=[MinLengthValidator(MIN_LENGTH_MODEL),],
    )
    year = models.IntegerField(
                               validators=[validate_year_value,],
                               blank=False, null=False,
    )
    image_url = models.URLField(
                                null=False, blank=False, unique=True,
    )
    price = models.FloatField(
                              null=False, blank=False,
                              validators=[MinValueValidator(MIN_VALUE_PRICE),],
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE,)
