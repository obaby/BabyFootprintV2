# Generated by Django 3.2.3 on 2024-11-19 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FootPrint', '0005_mapsetting'),
    ]

    operations = [
        migrations.AddField(
            model_name='markerimage',
            name='place_holder_image_url',
            field=models.URLField(blank=True, help_text='占位图片', null=True),
        ),
    ]
