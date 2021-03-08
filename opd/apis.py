from rest_framework import status, serializers, permissions, viewsets
import datetime
from .models import Services, BillDetails, BillHeader
from .serializers import ServiceSerializer, BillDetailsSerializer, BillHeaderSerializer, PatientsSerializer

from users.models import Patients

class all_service(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]

    queryset = Services.objects.all()


class TodayBillDetails(viewsets.ModelViewSet):
    serializer_class = BillDetailsSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        today = datetime.date.today()

        return BillDetails.objects.filter(create_at__date = today)


class TodayBillHeader(viewsets.ModelViewSet):
    serializer_class = BillHeaderSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        today = datetime.date.today()
        return BillHeader.objects.filter(create_at__date=today)

class TodayPatients(viewsets.ModelViewSet):
    serializer_class = PatientsSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Patients.objects.all()


