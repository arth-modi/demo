# Generated by Django 4.2.11 on 2024-05-01 04:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_register', '0009_remove_employee_emp_registe_fullnam_102cb3_idx_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 1, 4, 55, 53, 307722, tzinfo=datetime.timezone.utc)),
        ),
    ]