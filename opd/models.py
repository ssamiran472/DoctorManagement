from django.db import models
from users.models import Patients


class Services(models.Model):
    particular = models.CharField(max_length=100)
    charges = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.particular
    

def makeBillNumber():
    totalHeader = BillHeader.objects.all().count()
    if totalHeader <10:
        return '000' + str(totalHeader)
    elif totalHeader < 100:
        return '00' + str(totalHeader)
    elif totalHeader < 1000:
        return '0' + str(totalHeader)
    return totalHeader



class BillHeader(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    billNo = models.CharField(default=makeBillNumber, max_length=100)
    isFinalise = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(default='', max_length=100, blank=True)

    def __str__(self):
        return '{0}({1})'.format(self.patient.full_name, self.get_date)
    
    def get_date(self):
        return self.create_at.strftime("%m/%d/%Y")



class BillDetails(models.Model):
    amount = models.PositiveIntegerField(default=0)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)












