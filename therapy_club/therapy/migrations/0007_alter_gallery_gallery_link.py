# Generated by Django 4.2.3 on 2023-07-11 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('therapy', '0006_gallery_gallery_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='gallery_link',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, related_name='category_photo', to='therapy.servicecategory', verbose_name='к какой категории фото'),
        ),
    ]
