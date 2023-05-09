# Generated by Django 4.2 on 2023-05-09 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('masters', '0016_medicaltest_is_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalTestSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(max_length=4)),
                ('session', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalTestProfilePerSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medical_test_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_test_profile_per_session', to='masters.medicaltestprofile')),
                ('medical_test_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_test_profile_per_session', to='configuration.medicaltestsession')),
            ],
        ),
    ]
