from django.forms import ModelForm
from . models import Person

class RegiForm(ModelForm):
    class Meta:
        model = Person
        fields='__all__'

#project, models, processing,what u gonna do, python processing        