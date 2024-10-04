from django.core.exceptions import ValidationError


def validate_year_value(year):
    if 1999 > year > 2030:
        raise ValidationError("Year must be between 1999 and 2030!")