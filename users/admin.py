from django.contrib import admin
from .models import Patients, Consultants, User

admin.site.register((Patients, Consultants, User))