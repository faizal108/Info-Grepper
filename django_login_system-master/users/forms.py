from .models import Profile
from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(max_length=120)
    birth_date = forms.DateField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',
                  'birth_date', 'password1', 'password2')

    # def __init__(self, *args, **kwargs):
    #     super(SignupForm,self).__init__(*args, **kwargs)

    #     self.fields['username'].widget.attrs['class'] = 'form-control'


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(max_length=120)
    birth_date = forms.DateField(
        required=False, widget=forms.TextInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'birth_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['birth_date'].initial = self.instance.profile.birth_date

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Email', max_length=254)
