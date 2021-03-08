from django.shortcuts import render
import datetime



from users.models import Patients
from .forms import PatientsForm, PatientsUhiForm



def index(request):
    return render(request, 'index.html')

def todayOpdPatients(request):
    context ={}
    today = datetime.date.today()
    # today_patient= Patients.objects.filter(created_at__year = today.year, created_at__month=today.month)
    if(request.method == 'POST'):
        print(request.POST)
        form = PatientsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    # today_patient = Patients.objects.filter(created_at__date=today)
    today_patient = Patients.objects.all()
    context['patients'] = today_patient
    context['form'] = PatientsUhiForm()
    
    return render(request, 'todayOPDPatients.html', context)


def old_patients(request):
    context={}
    patients = Patients.objects.all()
    context['patients'] = patients
    context['form'] = PatientsUhiForm()
    
    return render(request, 'oldPatients.html', context)
