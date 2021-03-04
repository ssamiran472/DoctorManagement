from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import date, datetime
# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, user_type, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('Email must be needed.')
        
        if not user_type:
            raise ValueError('User type must be needed.')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,email, user_type, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user( email, password, **extra_fields)

    def create_superuser(self,email, user_type, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email,user_type, password, **extra_fields)



class User(AbstractBaseUser):
    choices = (
        ('A', 'Admin'),
        ('D', 'Doctor'),
        ('R', 'Receptionist'),
        ('L', 'lab'),

    )
    Full_name = models.CharField(max_length = 150, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length = 150, blank=True, null=True)
    user_type = models.CharField(max_length=1, choices=choices)
    profile_pic = models.ImageField(blank=True, null=True)
    registered_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_type']
    
    objects = UserManager()


    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser


class Consultants(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    Fees = models.PositiveIntegerField(default=0)
    Gender = models.CharField(max_length=10)
    Dob = models.CharField(max_length=20)
    Mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    

def creatUhid():
    dates = date.today()
    year = dates.year
    total_patients = Patients.objects.filter(created_at__year = year).count()
    if total_patients < 9:
        text = '{0}/000{1}'.format(str(year), str(total_patients+1))
    elif (total_patients <99) and (total_patients >=10):
        text = '{0}/00{1}'.format(str(year), str(total_patients+1))

    elif (total_patients <999 ) and (total_patients >=100):
        text = '{0}/0{1}'.format(str(year), str(total_patients+1))
    
    else:
        text = '{0}/{1}'.format(str(year), str(total_patients+1))
    
    return text






class Patients(models.Model):

    UhidNo = models.CharField(default=creatUhid, max_length=100)
    title = models.CharField(max_length=10)
    surname = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50, default='', blank=True)
    BirthDate = models.DateField(null=True, blank=True)
    patient_status = models.CharField(max_length=15, default='N', blank=True)
    Age = models.IntegerField(default=0)
    gender = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    tell_no = models.CharField(max_length=10)
    ref_by = models.CharField(max_length=100)
    paymentBy = models.CharField(max_length=10)
    Consultants=models.ForeignKey(Consultants, on_delete=models.CASCADE)
    id_proof_name = models.CharField(max_length=100)
    id_prof_details = models.CharField(max_length=20)
    Weight = models.DecimalField(max_digits=10, decimal_places=3, default=0.000)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)









