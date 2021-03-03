from django.shortcuts import render
import datetime



from users.models import Patients
from .forms import PatientsForm



def index(request):
    return render(request, 'index.html')

def todayOpdPatients(request):
    context ={}
    today = datetime.date.today()
    # today_patient= Patients.objects.filter(created_at__year = today.year, created_at__month=today.month)
    today_patient = Patients.objects.all()
    context['patients'] = today_patient
    context['form'] = PatientsForm()
    if(request.method == 'POST'):
        form = PatientsForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'todayOPDPatients.html', context)

