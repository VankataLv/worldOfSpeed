from django.core.validators import MinValueValidator
from django.db import models

from worldOfSpeed.profiles.validators import validate_chars_username, validate_username_length


class Profile(models.Model):
    MAX_LENGTH_USERNAME = 15
    MIN_VALUE_AGE = 21
    MAX_LENGTH_PASSWORD = 20
    MAX_LENGTH_FIRST_NAME = 25
    MAX_LENGTH_LAST_NAME = 25

    username = models.CharField(max_length=MAX_LENGTH_USERNAME,
                                null=False, blank=False,
                                validators=[validate_chars_username, validate_username_length],
    )
    email = models.EmailField(
                              null=False, blank=False,
    )
    age = models.IntegerField(
        help_text="Age requirement: 21 years and above.",
        validators=[MinValueValidator(MIN_VALUE_AGE),],
    )
    password = models.CharField(
        null=False, blank=False,
        max_length=MAX_LENGTH_PASSWORD,
    )
    first_name = models.CharField(
        null=True, blank=True,
        max_length=MAX_LENGTH_FIRST_NAME,
    )
    last_name = models.CharField(
        null=True, blank=True,
        max_length=MAX_LENGTH_LAST_NAME,
    )
    profile_picture = models.URLField(
        null=True, blank=True,
    )

    @property
    def full_name_setup(self):
        full_name = ""
        if self.first_name and self.last_name:
            full_name = self.first_name + " " + self.last_name
        elif self.first_name and not self.last_name:
            full_name = self.first_name
        elif not self.first_name and self.last_name:
            full_name = self.last_name
        return full_name
