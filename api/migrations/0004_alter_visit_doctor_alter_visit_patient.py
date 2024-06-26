# Generated by Django 5.0.3 on 2024-03-28 20:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_specialization_remove_doctor_additional_information_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='api.doctor'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='api.patient'),
        ),
    ]
