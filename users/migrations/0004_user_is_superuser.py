# Generated by Django 3.1.7 on 2021-03-02 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
