# Generated by Django 5.0.6 on 2024-07-09 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_address_city_country_comments'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]
