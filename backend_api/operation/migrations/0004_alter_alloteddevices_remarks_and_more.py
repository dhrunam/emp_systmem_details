# Generated by Django 4.2.2 on 2024-06-19 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0003_alter_systemassignmentdetails_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alloteddevices',
            name='remarks',
            field=models.CharField(default='', max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='systemassignmentdetails',
            name='remarks',
            field=models.CharField(default='', max_length=1024, null=True),
        ),
    ]
