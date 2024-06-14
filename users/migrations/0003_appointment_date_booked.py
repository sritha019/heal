# Generated by Django 5.0.6 on 2024-06-13 12:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_doctor_testcategory_appointment_report_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='date_booked',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
