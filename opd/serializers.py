from rest_framework import serializers

from .models import Services, BillHeader, BillDetails
from .models import Patients


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class BillHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillHeader
        fields = '__all__'

class BillDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillDetails
        fields = '__all__'


class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = '__all__'
        