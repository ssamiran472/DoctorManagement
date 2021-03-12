import datetime
from django.db import models
from users.models import Patients, Consultants


class Services(models.Model):
    particular = models.CharField(max_length=100)
    charges = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.particular
    

def makeBillNumber():
    today = datetime.date.today()
    totalHeader = BillHeader.objects.filter(created_at__date = today).count()
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
    total_bill = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    # def __str__(self):
    #     return '{0}({1})'.format(self.patient.full_name, self.get_date)
    
    def get_date(self):
        return self.create_at.strftime("%m/%d/%Y")



class BillDetails(models.Model):
    amount = models.PositiveIntegerField(default=0)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    user = models.CharField(max_length=100, default='')
    bill_header = models.ForeignKey(BillHeader, on_delete=models.CASCADE, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)



class OpdPatients(models.Model):
    '''
        HERE ONLY A PATIENT AND A DOCTOR DATA WILL BE SAVE FOR OPD PATIENT DATA.
    '''
    patients = models.ForeignKey(Patients, on_delete=models.CASCADE)
    consultants = models.ForeignKey(Consultants, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)








