# Generated by Django 3.1.7 on 2021-03-07 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_patients_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='patient_status',
            field=models.CharField(blank=True, default='N', max_length=15),
        ),
    ]
