from django import forms
from worldOfSpeed.cars.models import Car


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ('owner',)
        widgets = {
            'image_url': forms.URLInput(attrs={'placeholder': 'https://...'})
        }


class CarEditForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ('owner',)


class CarDeleteForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
