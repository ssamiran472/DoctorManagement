from users.models import Patients
from django import forms

class PatientsForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = '__all__'
