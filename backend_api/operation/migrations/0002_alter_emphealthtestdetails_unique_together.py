# Generated by Django 4.2 on 2023-06-21 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0002_employee_gender_alter_employee_blood_group'),
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='emphealthtestdetails',
            unique_together={('emp_health_profile_test', 'medical_test_profile', 'medical_test')},
        ),
    ]
