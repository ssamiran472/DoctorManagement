from django.contrib import admin
from .models import Patients, Consultants

admin.site.register((Patients, Consultants))