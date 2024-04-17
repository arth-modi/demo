# Generated by Django 4.2.11 on 2024-04-17 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_register', '0005_merge_20240416_0633'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='employee',
            index=models.Index(fields=['fullname', 'emp_code', 'mobile', 'email', 'position'], name='emp_registe_fullnam_102cb3_idx'),
        ),
    ]
