# Generated by Django 5.0.3 on 2024-04-02 15:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_schedule_patient_remove_visit_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='rating',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='visit',
            name='schedule',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='visits', to='api.schedule'),
        ),
    ]
