# Generated by Django 3.2.15 on 2022-09-26 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_rename_zipcode_listing_postal_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='state',
            new_name='province',
        ),
    ]
