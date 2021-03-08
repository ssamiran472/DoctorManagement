from django.contrib import admin
from .models import Services, BillHeader, BillDetails

admin.site.register((Services, BillHeader, BillDetails))
