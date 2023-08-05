# Generated by Django 4.2.3 on 2023-08-03 19:49

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therapy', '0009_merge_20230804_0240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commercial',
            name='icon',
        ),
        migrations.AlterField(
            model_name='commercial',
            name='about',
            field=models.CharField(blank=True, max_length=100, verbose_name='Слоган для ссылки'),
        ),
        migrations.AlterField(
            model_name='services',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Описание'),
        ),
    ]