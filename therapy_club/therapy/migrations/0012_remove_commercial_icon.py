# Generated by Django 4.2.3 on 2023-08-03 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('therapy', '0011_commercial_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commercial',
            name='icon',
        ),
    ]
