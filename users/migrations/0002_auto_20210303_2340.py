# Generated by Django 3.1.7 on 2021-03-03 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='middleName',
            field=models.CharField(default='', max_length=50),
        ),
    ]