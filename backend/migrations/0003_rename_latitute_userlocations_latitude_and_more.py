# Generated by Django 4.0.3 on 2022-03-13 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_userlocations_city_userlocations_country_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userlocations',
            old_name='latitute',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='userlocations',
            old_name='longitute',
            new_name='longitude',
        ),
    ]