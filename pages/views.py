from django.shortcuts import render
import datetime

from django.http import Http404


from users.models import Patients, Consultants
from .forms import PatientsForm, PatientsUhiForm
from opd.models import OpdPatients


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
            patient = form.save()
            consultant = request.POST['consultants']
            try:
                doctor = Consultants.objects.get(id=consultant)
                opd_patient = OpdPatients(patients=patient, consultants=doctor)
                opd_patient.save()
            except Consultants.DoesNotExist as e:
                raise Http404
            except Exception as e:
                print(e)

        else:
            print(form.errors)

    # today_patient = Patients.objects.filter(created_at__date=today)
    today_patient = Patients.objects.all()
    context['patients'] = today_patient
    context['form'] = PatientsUhiForm()
    context['consultants'] = Consultants.objects.all()
    print(Consultants.objects.all())
    return render(request, 'todayOPDPatients.html', context)


def old_patients(request):
    context={}
    patients = Patients.objects.all()
    context['patients'] = patients
    context['form'] = PatientsUhiForm()
    
    return render(request, 'oldPatients.html', context)
