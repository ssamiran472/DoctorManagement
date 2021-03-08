from django.urls import path, include
from rest_framework import routers

from .apis import TodayBillDetails, TodayBillHeader, all_service, TodayPatients


router = routers.DefaultRouter()

router.register('all_services', all_service, 'all_service')
router.register('TodayBillDetails', TodayBillDetails, 'TodayBillDetails')
router.register('TodayBillHeader', TodayBillHeader, 'TodayBillHeader')
router.register('TodayPatients', TodayPatients, 'TodayPatients')




urlpatterns = [
    path('', include(router.urls))
]
