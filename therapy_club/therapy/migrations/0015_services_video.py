# Generated by Django 4.2.3 on 2023-08-03 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therapy', '0014_abonements'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='images/%Y/%m/%d', verbose_name='видео (если есть)'),
        ),
    ]