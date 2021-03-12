from django.contrib import admin
from .models import Services, BillHeader, BillDetails, OpdPatients

admin.site.register((Services, BillHeader, BillDetails, OpdPatients))
