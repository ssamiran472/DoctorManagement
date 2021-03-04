from users.models import Patients, Consultants
from django import forms

class PatientsForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = '__all__'
        
class PatientsUhiForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = ('UhidNo', 'Consultants')