# Generated by Django 3.2.15 on 2022-09-26 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_rename_state_listing_province'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='lot_size',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_main',
            field=models.ImageField(upload_to='media/home_photos/%Y/%m/%d/'),
        ),
    ]
