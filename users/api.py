from django.http import JsonResponse, HttpResponse
from django.db.models import Q
from .models import Patients


from opd.serializers import PatientsSerializer



def searchPatient(request):
    name = request.GET.get('name')
    names = name.split(' ')
    patients = Patients.objects.all()
    patient_id = set()
    for i in names:
        patientSet = patients.filter(Q(firstName__istartswith=i) | Q(surname__istartswith=i))
        arr = []
        for pat in patientSet:
            arr.append(pat.id)
        arr = set(arr)
        patient_id.update(arr)

    returned_pat = patients.filter(id__in = patient_id)
    serializer = PatientsSerializer(returned_pat, many=True)
    return JsonResponse(serializer.data, safe=False)
