# Generated by Django 3.2.15 on 2022-09-27 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0004_alter_realtor_hire_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='photo',
            field=models.ImageField(upload_to='agent_photos/%Y/%m/%d/'),
        ),
    ]
