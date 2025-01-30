from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Projection

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class ProjectionForm(ModelForm):
        class Meta:
            model = Projection
            fields = ['film_name', 'film_time', 'capacity']