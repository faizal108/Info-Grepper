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
        fields = ('username', 'first_name', 'last_name', 'email', 'birth_date', 'password1', 'password2')
    
    # def __init__(self, *args, **kwargs):
    #     super(SignupForm,self).__init__(*args, **kwargs)

    #     self.fields['username'].widget.attrs['class'] = 'form-control'