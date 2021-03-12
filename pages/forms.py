from users.models import Patients, Consultants
from django import forms

class PatientsForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = '__all__'
        
class PatientsUhiForm(forms.ModelForm):
    # disabled_fields = ('UhidNo',)
    # def __init__(self, *args, **kwargs):
    #     super(PatientsUhiForm, self).__init__(*args, **kwargs)
    #     for field in self.disabled_fields:
    #         self.fields[field].disabled = True

    class Meta:
        model = Patients
        fields = ('UhidNo',)
        