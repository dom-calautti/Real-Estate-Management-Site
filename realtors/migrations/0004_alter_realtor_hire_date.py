# Generated by Django 3.2.15 on 2022-09-26 22:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0003_auto_20220926_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]