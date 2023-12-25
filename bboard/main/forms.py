from django.contrib.auth.forms import UserCreationForm

from .models import CustUser


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = CustUser
        fields = ["username", "email", "password1", "password2"]
