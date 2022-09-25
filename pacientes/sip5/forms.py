from dataclasses import fields
from django import forms
from .models import Paciente

class LibroForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'

