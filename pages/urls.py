from django.urls import path

from . import views



urlpatterns = [
    path('', views.index, name="index"),
    path('today-opd-patients/', views.todayOpdPatients, name="todayOpdPatients"),
    path('old-patients/', views.old_patients, name='old_patients'),
    
]
