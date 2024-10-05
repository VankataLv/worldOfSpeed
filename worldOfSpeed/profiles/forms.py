from django import forms
from worldOfSpeed.profiles.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = 'username','email', 'age', 'password',
        help_texts = {
            'age': "Age requirement: 21 years and above."
        }
        widgets = {
            'password': forms.PasswordInput(),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()